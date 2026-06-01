
# Corporate Payment Aggregation & Feature Engineering Pipeline

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Preparation-pandas.svg)]()
[![Analytics](https://img.shields.io/badge/Domain-Time%20Series%20%7C%20EDA-blueviolet.svg)]()

## 📌 Project Overview
This project delivers a data-engineering pipeline designed to process highly skewed, sparse transactional payment systems into clean, month-end aggregated features ready for machine learning algorithms.

The repository showcases advanced data preprocessing steps, including handling structured sparsity, multi-level categorical resampling, and variance stabilization techniques to mitigate the impact of extreme financial outliers.

## 🛠️ Technical Implementation & Methodology

* **Sparsity Correction:** Reconstructed a dataset of **106,016 observations** by treating implicit systemic missingness (`NaN`) in payment channels as explicit operational zero-values (`.fillna(0)`).
* **Multi-Categorical Resampling:** Aggregated granular transactional rows using multi-key grouping (`Class`, `Test`) combined with standard Month-End calendar frequency (`'ME'`).
* **Variance Stabilization via $Log(1+X)$:** Addressed non-linear scale expansion typical for banking data, mapping values mathematically to control target volatility.

---

## 📊 Statistical Analysis & Transformation Results

The pipeline successfully transforms unstable financial indicators into standardized analytical variables:

### 1. Raw Aggregated Metrics (Extreme Skewness)
Before stabilization, the multi-level monthly aggregates demonstrated high volatility driven by extreme corporate actions:
* **Total Payment Median (50%):** 100.00
* **Total Payment Max:** 146,715.00
* **Standard Deviation ($\sigma$):** 15,624.71 *(indicating a heavy-tailed, highly un-skewed distribution where $\sigma \gg \mu$)*

### 2. Log-Transformed Metrics (Model-Ready Distribution)
Applying the monotonic log-transformation $Y = \ln(1 + X)$ compressed the feature space to dynamic scaling boundaries, eliminating massive gradient step penalties for future loss functions:
* **Total Payment Max (Scaled):** 11.89
* **Standard Deviation ($\sigma$ Scaled):** 3.88
* **Skewness Mitigation:** The mathematical distance between the 50th percentile and the Maximum value was reduced from a factor of $1400\times$ to less than $3\times$.

```text
--- Distribution Scaling Impact ---
Metric          | Raw Value Max | Log1P Value Max | Final Std Dev (Sigma)
-------------------------------------------------------------------------
Pay_Type_1      | 146,265.00    | 11.89           | 3.69
Pay_Type_2      |  45,025.00    | 10.71           | 3.23
Total_Payment   | 146,715.00    | 11.89           | 3.88
```

## 🚀 Pipeline Execution
Setup and Dependencies
Ensure you have the core analytics stack installed:
* pip install pandas numpy seaborn matplotlib

## Run Pipeline
Execute the processing sequence to clean, aggregate, log-transform, and export the structured dataset:
* python payment_pipeline.py


###📂 Project Structure
* pay_demo.csv         # Raw payment history (omitted via .gitignore for confidentiality)
* payment_pipeline.py  # Python script containing cleaning, aggregation, and log1p execution
* sample.csv           # Final processed, variance-stabilized output file
* requirements.txt     # List of dependencies
* README.md            # Technical case-study documentation
