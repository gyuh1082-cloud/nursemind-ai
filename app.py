import streamlit as st

st.set_page_config(page_title="NurseMind AI", page_icon="🩺", layout="centered")

st.title("NurseMind AI 🩺")
st.subheader("Clinical Risk and Nursing Priorities Simulator")

st.write(
    "This project simulates how nurses identify patient safety concerns, "
    "priority actions, and education needs based on a patient scenario."
)

age = st.number_input("Patient age:", min_value=0, max_value=120, value=70)

symptoms = st.text_area(
    "Enter symptoms:",
    placeholder="Example: dizziness, weakness, cough, fever, shortness of breath"
)

systolic_bp = st.number_input("Systolic blood pressure:", min_value=50, max_value=250, value=120)
temperature = st.number_input("Temperature (F):", min_value=90.0, max_value=110.0, value=98.6)
oxygen = st.number_input("Oxygen saturation (%):", min_value=50, max_value=100, value=98)

medications = st.text_area(
    "Enter medications:",
    placeholder="Example: blood pressure medication, antibiotic"
)

if st.button("Analyze Patient Case"):
    risk_flags = []
    actions = []
    education = []
    escalation = "Low"

    s = symptoms.lower()
    m = medications.lower()

    if age >= 65 and "dizziness" in s:
        risk_flags.append("Fall risk")
        actions.append("Assist patient with walking and prevent unassisted ambulation")
        education.append("Stand up slowly and ask for help before walking")

    if systolic_bp < 95:
        risk_flags.append("Low blood pressure concern")
        actions.append("Recheck blood pressure and assess for weakness or fainting")
        education.append("Report worsening dizziness, fainting, or weakness")

    if "fever" in s or temperature >= 100.4:
        risk_flags.append("Possible infection")
        actions.append("Monitor temperature and watch for worsening symptoms")
        education.append("Take medicine exactly as prescribed and report worsening fever")

    if "cough" in s and oxygen < 94:
        risk_flags.append("Respiratory concern")
        actions.append("Monitor breathing and oxygen status closely")
        education.append("Seek help right away for trouble breathing")
        escalation = "High"

    if "shortness of breath" in s:
        risk_flags.append("Breathing difficulty")
        actions.append("Assess breathing immediately")
        education.append("Call for urgent help if breathing gets worse")
        escalation = "High"

    if "weakness" in s and ("vomiting" in s or "diarrhea" in s):
        risk_flags.append("Dehydration risk")
        actions.append("Monitor fluid intake and signs of dehydration")
        education.append("Drink fluids if allowed and report worsening weakness")

    if "antibiotic" in m and "dizziness" in s:
        risk_flags.append("Possible medication side effect")
        actions.append("Review recent medication changes")
        education.append("Ask your provider if symptoms started after a new medicine")

    if age >= 65 and "confusion" in s:
        risk_flags.append("Urgent mental status change")
        actions.append("Assess patient immediately and notify provider")
        education.append("New confusion should be reported right away")
        escalation = "High"

    if not risk_flags:
        risk_flags.append("No major high-risk flags detected from current inputs")
        actions.append("Continue routine monitoring")
        education.append("Follow provider instructions and report new symptoms")

    st.markdown("## Risk Flags")
    for item in risk_flags:
        st.write(f"- {item}")

    st.markdown("## Priority Nursing Actions")
    for item in actions:
        st.write(f"- {item}")

    st.markdown("## Patient Education")
    for item in education:
        st.write(f"- {item}")

    st.markdown("## Escalation Level")
    st.write(escalation)

st.markdown("---")
st.caption(
    "Disclaimer: This project is for educational purposes only. "
    "It does not diagnose, treat, or replace professional medical judgment."
)
