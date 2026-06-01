# Time-Series Payment Data Aggregation & EDA Pipeline

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Engineering-pandas.svg)]()
[![Data Analytics](https://img.shields.io/badge/Phase-Data%20Preparation%20%26%20EDA-green.svg)]()

## 📌 Project Overview
This project establishes a robust data engineering and preprocessing pipeline designed to transform raw, transactional payment records into structured, 
monthly aggregated features suitable for predictive modeling (time-series forecasting). 
It addresses common data-quality issues such as missing temporal records, unaligned payment types, and extreme variance in data distributions.

## 🛠️ Tech Stack & Key Operations
* **Libraries:** `pandas`, `numpy`
* **Data Engineering Techniques:**
  * **Data Cleansing:** Handling structural missing values (NaNs) in chronological checkpoints and financial metrics.
  * **Feature Engineering:** Dynamic column vectorization to compute absolute corporate metrics (`Total_Payment`).
  * **Time-Series Resampling:** Multi-level categorical grouping paired with monthly frequency resampling (`'ME'`).

---

## 📈 Data Pipeline Architecture

### 1. Data Cleaning & Alignment
* Identified and removed incomplete records lacking essential `Date` signatures to protect timeline integrity.
* Vectorized `NaN` fill-operations on specific granular sources (`Pay_Type_1`, `Pay_Type_2`) preventing structural loss during calculation steps.

### 2. Multi-Level Grouping & Resampling
To prepare features for future machine learning forecasting (e.g., ARIMA, Prophet, or XGBoost Regressor), individual granular transactions are scaled using a combination of categorical features and calendar frequencies:
* Grouped by unique segment slices: `Class` and `Test`.
* Resampled chronologically using Month-End (`ME`) anchors.
* Executed deterministic feature aggregations via `.agg(['sum'])`.

### 3. Distribution & Outlier Analysis
* Implemented distribution mapping using **Seaborn Boxplots** to identify outliers and evaluate dispersion metrics across payment classes.
* Designed a feature scale stabilizer using log-transformation:
  $$Y = \ln(1 + X)$$
  *This handles heavy-tailed financial distributions and stabilizes variance across highly skewed fields.*

---

## 🚀 How to Replicate

1. Clone this repository:
   ```bash
   git clone [https://github.com/your-username/payment-data-pipeline-eda.git](https://github.com/your-username/payment-data-pipeline-eda.git)
   cd payment-data-pipeline-eda
