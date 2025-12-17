# systemic-justice-gap-analyzer
# Systemic Justice Gap Identification using FP-Growth Association Rule Mining

## Overview
This project implements an **interpretable machine learning framework** for identifying **systemic justice gaps** in legal case data using **FP-Growth Association Rule Mining with Lift-Based Interestingness Filtering**.

Unlike black-box predictive models, the system focuses on **transparent, rule-based insights** that can support policy analysis, institutional reform, and academic research in legal analytics.

The project is aligned with an **academic research paper and a provisional patent**, and is deployed as a **live interactive dashboard using Streamlit and GitHub**.

---

## Problem Statement
Public legal systems often suffer from **systemic inefficiencies**, such as:
- Procedural delays  
- Outcome disparities across case types or regions  
- Institutional bottlenecks  

Traditional legal analytics approaches rely on predictive models that lack interpretability. This project addresses the gap by using **association rule mining** to uncover **human-readable patterns** that indicate justice gaps.

---

## Proposed Solution
The system applies the following pipeline:

1. **Dataset Engineering**
   - Legal judgment data is transformed into policy-relevant categorical features
   - Explicit justice-gap indicators are derived (delay and unfavorable outcomes)

2. **FP-Growth Mining**
   - Efficient discovery of frequent institutional patterns
   - Avoids candidate generation used in Apriori

3. **Lift-Based Filtering**
   - Filters rules that significantly deviate from baseline expectations
   - Emphasizes systemic disparity rather than frequency alone

4. **Justice Gap Analyzer**
   - Computes baseline probabilities
   - Calculates adjusted lift
   - Categorizes and ranks justice gaps by severity

5. **Interactive Dashboard**
   - Streamlit-based interface
   - Live filtering and exploration of justice-gap rules

---

## Technologies Used
- **Python**
- **Pandas, NumPy**
- **mlxtend (FP-Growth & Association Rules)**
- **Joblib**
- **Streamlit**
- **GitHub & Streamlit Cloud**

---

## Project Structure
