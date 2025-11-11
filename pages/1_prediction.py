import streamlit as st
import numpy as np
import pandas as pd
import joblib

st.set_page_config(page_title="Crush Predictor", page_icon="💘")

st.title("🔮 Crush Likelihood Prediction")
st.write("Select values (1–10) based on your experiences:")

# Load model
model = joblib.load("model/crush_predictor_model.pkl")

questions = [
    ("initiates_conversation", "💬 Do they start conversations with you?"),
    ("engagement", "🎧 Do they seem interested when you talk?"),
    ("quick_responses", "📱 Do they reply quickly to your messages?"),
    ("eye_contact", "👀 Do they make eye contact often?"),
    ("joke_responses", "😄 Do they joke around with you?"),
    ("nervous", "😬 Do they seem nervous around you sometimes?"),
    ("stays_near_you", "🧍‍♂️ Do they stay close to you in groups?"),
    ("helps_you", "🤝 Do they help you when you need it?"),
    ("smiles", "😊 Do they smile a lot around you?"),
    ("takes_you_out", "🎉 Do they invite you to hang out?")
]

columns = [q[0] for q in questions]

with st.form("prediction_form"):
    drops = []

    # ---- ROW 1 (4 inputs) ----
    r1 = st.columns(4)
    for i in range(4):
        key, q = questions[i]
        val = r1[i].selectbox(q, list(range(1, 11)))
        drops.append(val)

    # ---- ROW 2 (4 inputs) ----
    r2 = st.columns(4)
    for i in range(4, 8):
        key, q = questions[i]
        val = r2[i-4].selectbox(q, list(range(1, 11)))
        drops.append(val)

    # ---- ROW 3 (2 inputs) ----
    r3 = st.columns(2)
    for i in range(8, 10):
        key, q = questions[i]
        val = r3[i-8].selectbox(q, list(range(1, 11)))
        drops.append(val)

    submitted = st.form_submit_button("Predict ❤️")

if submitted:
    df = pd.DataFrame([drops], columns=columns)
    result = float(model.predict(df)[0])

    st.subheader(f"💘 Your crush’s likelihood is: **{result:.2f}%**")

    # Reaction images
    if result < 45:
        st.image("images/low.jpg", width=350)
        st.info("Yea sbb karne aate ho skool ?, padai pr dhyan de lo thoda! 😄")

    elif result < 75:
        st.image("images/mid.jpeg", width=350)
        st.warning("Decent chance! Kuch toh connection hai! 😉")

    else:
        st.image("images/high.jpg", width=350)
        st.success("High chances! Time to shoot your shot ❤️🔥")
