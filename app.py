
import streamlit as st
import pandas as pd
import joblib

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Systemic Justice Gap Analyzer",
    layout="wide"
)

st.title("Systemic Justice Gap Identification Dashboard")
st.markdown(
    """
    This dashboard presents **interpretable justice-gap patterns**
    discovered using **FP-Growth Association Rule Mining with Lift-Based Filtering**.
    """
)

# --------------------------------------------------
# Load Model Output
# --------------------------------------------------
@st.cache_data
def load_data():
    return joblib.load("justice_gap_analyzer.pkl")

df = load_data()

# --------------------------------------------------
# Sidebar Filters
# --------------------------------------------------
st.sidebar.header("Filter Rules")

gap_category = st.sidebar.multiselect(
    "Justice Gap Category",
    options=df["gap_category"].unique(),
    default=list(df["gap_category"].unique())
)

gap_severity = st.sidebar.multiselect(
    "Gap Severity",
    options=df["gap_severity"].unique(),
    default=list(df["gap_severity"].unique())
)

min_lift = st.sidebar.slider(
    "Minimum Adjusted Lift",
    min_value=float(df["adjusted_lift"].min()),
    max_value=float(df["adjusted_lift"].max()),
    value=1.3,
    step=0.1
)

# --------------------------------------------------
# Apply Filters
# --------------------------------------------------
filtered_df = df[
    (df["gap_category"].isin(gap_category)) &
    (df["gap_severity"].isin(gap_severity)) &
    (df["adjusted_lift"] >= min_lift)
]

# --------------------------------------------------
# Display Summary Metrics
# --------------------------------------------------
st.subheader("Summary Statistics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Rules", len(filtered_df))
col2.metric("High Severity Gaps", len(filtered_df[filtered_df["gap_severity"] == "High"]))
col3.metric("Max Adjusted Lift", round(filtered_df["adjusted_lift"].max(), 2))

# --------------------------------------------------
# Rule Table
# --------------------------------------------------
st.subheader("Justice Gap Rules")

st.dataframe(
    filtered_df[
        [
            "antecedents",
            "consequents",
            "gap_category",
            "gap_severity",
            "support",
            "confidence",
            "lift",
            "adjusted_lift"
        ]
    ],
    use_container_width=True
)

# --------------------------------------------------
# Interpretation Panel
# --------------------------------------------------
st.subheader("How to Interpret")

st.markdown(
    """
    - **Antecedents**: Institutional or procedural conditions  
    - **Consequents**: Justice gap indicators (delay or unfavorable outcome)  
    - **Lift**: Deviation from independence  
    - **Adjusted Lift**: Excess risk compared to case-type baseline  

    **Adjusted Lift > 1.5** indicates a potential *systemic anomaly* requiring policy attention.
    """
)
