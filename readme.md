# 🧠 Mental Health Risk Predictor

## 📌 Project Overview
This project predicts the likelihood of an individual being **at risk of mental health issues** (e.g., depression, anxiety, burnout) using:
- **Survey data** (demographics, workplace environment, prior mental health history)
- **Passive behavioral data (simulated)** like sleep hours, screen time, and physical activity.

The main goal is to showcase skills in **EDA, feature engineering, machine learning, and model explainability** for Data Scientist roles.

-------------------------------------------------------------------

## 🎯 Key Features
- **EDA**: Explored distributions, correlations, and key trends in the OSMI Mental Health in Tech Survey dataset.
- **Target Engineering**: Created a binary classification label (`at_risk`) from survey responses.
- **Modeling**: Implemented Logistic Regression, Random Forest, and XGBoost.
- **Explainability**: Used SHAP values to interpret model decisions.
- **Deployment**: Built an interactive **Streamlit app** for real-time risk scoring.

-------------------------------------------------------------------

## 📊 Dataset
- **Source**: [Kaggle – Mental Health in Tech Survey](https://www.kaggle.com/datasets/osmi/mental-health-in-tech-survey)
- **Size**: ~1,250 responses
- **Target**: `at_risk` (1 = at risk, 0 = not at risk)

-------------------------------------------------------------------

## ⚙️ Tech Stack
- **Python**: pandas, numpy, scikit-learn
- **Visualization**: matplotlib, seaborn, shap
- **ML Models**: Logistic Regression, Random Forest, XGBoost
- **App**: Streamlit
- **Environment**: Anaconda + pip

-------------------------------------------------------------------

## 🚀 How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/mental-health-risk-predictor.git
   cd mental-health-risk-predictor
