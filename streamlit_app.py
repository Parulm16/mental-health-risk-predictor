import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/random_forest.pkl")

st.title("🧠 Mental Health Risk Predictor")
st.write("Predict likelihood of being at mental health risk based on survey + passive data.")

# Sidebar input
st.sidebar.header("User Input Features")

age = st.sidebar.slider("Age", 18, 65, 30)
gender = st.sidebar.selectbox("Gender", ("Male", "Female"))
family_history = st.sidebar.selectbox("Family History of Mental Illness", ("Yes", "No"))
work_hours = st.sidebar.slider("Work Hours per Week", 20, 80, 40)
sleep_hours = st.sidebar.slider("Average Sleep Hours", 3, 10, 7)
screen_time = st.sidebar.slider("Daily Screen Time (hours)", 1, 12, 5)

# Convert inputs to DataFrame
user_data = pd.DataFrame({
    'Age': [age],
    'Gender_Female': [1 if gender=="Female" else 0],
    'family_history_Yes': [1 if family_history=="Yes" else 0],
    'work_hours': [work_hours],
    'sleep_hours': [sleep_hours],
    'screen_time': [screen_time]
})

# Prediction
prob = model.predict_proba(user_data)[:,1][0]
risk = model.predict(user_data)[0]

st.subheader("Prediction Result")
st.write(f"Risk Probability: **{prob:.2f}**")
st.write("At Risk" if risk==1 else "Not at Risk")

# Wellness score
wellness_score = (1 - prob) * 100
st.progress(int(wellness_score))
st.write(f"Your Wellness Score: **{int(wellness_score)} / 100**")

# Simple tip
if sleep_hours < 6:
    st.warning("⚠️ Your sleep hours are low. Consider prioritizing rest.")
elif screen_time > 8:
    st.warning("⚠️ High screen time detected. Try reducing usage before bed.")
else:
    st.success("✅ Your lifestyle looks balanced!")
