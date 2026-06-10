import streamlit as st
import requests

st.set_page_config(page_title="Drug Risk Prediction")

st.title("💊 AI Drug Risk Prediction System")

Age = st.number_input("Age", value=0.0)
Nscore = st.number_input("Neuroticism Score", value=0.0)
Escore = st.number_input("Extraversion Score", value=0.0)
Oscore = st.number_input("Openness Score", value=0.0)
Ascore = st.number_input("Agreeableness Score", value=0.0)
Cscore = st.number_input("Conscientiousness Score", value=0.0)
Impulsive = st.number_input("Impulsiveness", value=0.0)
SS = st.number_input("Sensation Seeking", value=0.0)

if st.button("Predict Risk"):

    data = {
        "Age": Age,
        "Nscore": Nscore,
        "Escore": Escore,
        "Oscore": Oscore,
        "Ascore": Ascore,
        "Cscore": Cscore,
        "Impulsive": Impulsive,
        "SS": SS
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=data
    )

    result = response.json()

    risk = result["risk_probability"] * 100

    st.subheader("Prediction Result")

    if result["prediction"] == 1:
        st.error(f"High Risk ({risk:.2f}%)")
    else:
        st.success(f"Low Risk ({risk:.2f}%)")