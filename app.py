

st.set_page_config(page_title="NurseMind AI", page_icon="🩺", layout="centered")

st.title("NurseMind AI 🩺")
st.subheader("Clinical Risk and Nursing Priorities Simulator")

st.write(
    "This project simulates how nurses identify patient safety concerns, "
    "priority actions, and patient education needs from a patient case."
)

case_choice = st.selectbox(
    "Choose a sample patient case or enter your own:",
    ["Enter my own case", "Older adult with dizziness", "Respiratory concern", "Dehydration concern"]
)

if case_choice == "Older adult with dizziness":
    age = 78
    symptoms = "dizziness, weakness"
    systolic_bp = 92
    temperature = 98.7
    oxygen = 97
    medications = "blood pressure medication, antibiotic"
elif case_choice == "Respiratory concern":
    age = 66
    symptoms = "fever, cough, shortness of breath"
    systolic_bp = 108
    temperature = 101.3
    oxygen = 91
    medications = "inhaler"
elif case_choice == "Dehydration concern":
    age = 72
    symptoms = "weakness, vomiting, diarrhea"
    systolic_bp = 94
    temperature = 99.4
    oxygen = 98
    medications = "antibiotic"
else:
    age = 70
    symptoms = ""
    systolic_bp = 120
    temperature = 98.6
    oxygen = 98
    medications = ""

age = st.number_input("Patient age:", min_value=0, max_value=120, value=age)
symptoms = st.text_area("Symptoms:", value=symptoms)
systolic_bp = st.number_input("Systolic blood pressure:", min_value=50, max_value=250, value=systolic_bp)
temperature = st.number_input("Temperature (F):", min_value=90.0, max_value=110.0, value=float(temperature))
oxygen = st.number_input("Oxygen saturation (%):", min_value=50, max_value=100, value=oxygen)
medications = st.text_area("Medications:", value=medications)

if st.button("Analyze Patient Case"):
    risk_flags = []
    actions = []
    education = []
    reasons = []
    escalation = "Low"

    s = symptoms.lower()
    m = medications.lower()

    if age >= 65 and "dizziness" in s:
        risk_flags.append("Fall risk")
        actions.append("Assist with walking and prevent walking alone")
        education.append("Stand up slowly and ask for help before walking")
        reasons.append("Older age plus dizziness increases the chance of falling.")

    if systolic_bp < 95:
        risk_flags.append("Low blood pressure concern")
        actions.append("Recheck blood pressure and assess for fainting or weakness")
        education.append("Report fainting, worsening dizziness, or weakness")
        reasons.append("A low systolic blood pressure can reduce stability and cause dizziness.")

    if "fever" in s or temperature >= 100.4:
        risk_flags.append("Possible infection")
        actions.append("Monitor temperature and watch for worsening symptoms")
        education.append("Take medicine exactly as prescribed and report worsening fever")
        reasons.append("Fever may suggest infection or a worsening illness.")

    if "cough" in s and oxygen < 94:
        risk_flags.append("Respiratory concern")
        actions.append("Monitor breathing and oxygen level closely")
        education.append("Get help right away for trouble breathing")
        reasons.append("Cough with low oxygen can signal a breathing problem.")
        escalation = "High"

    if "shortness of breath" in s:
        risk_flags.append("Breathing difficulty")
        actions.append("Assess breathing immediately")
        education.append("Call for urgent help if breathing gets worse")
        reasons.append("Shortness of breath can become serious quickly.")
        escalation = "High"

    if "weakness" in s and ("vomiting" in s or "diarrhea" in s):
        risk_flags.append("Dehydration risk")
        actions.append("Monitor fluid intake and signs of dehydration")
        education.append("Drink fluids if allowed and report worsening weakness")
        reasons.append("Vomiting or diarrhea with weakness can lead to dehydration.")

    if "antibiotic" in m and "dizziness" in s:
        risk_flags.append("Possible medication side effect")
        actions.append("Review recent medication changes")
        education.append("Tell a provider when symptoms started after a new medicine")
        reasons.append("New symptoms after starting a medication may point to a side effect.")

    if age >= 65 and "confusion" in s:
        risk_flags.append("Urgent mental status change")
        actions.append("Assess patient immediately and notify provider")
        education.append("New confusion should be reported right away")
        reasons.append("Confusion in an older adult can be a serious warning sign.")
        escalation = "High"

    if not risk_flags:
        risk_flags.append("No major high-risk flags detected from current inputs")
        actions.append("Continue routine monitoring")
        education.append("Follow provider instructions and report new symptoms")
        reasons.append("The entered information did not trigger major safety rules.")

    st.markdown("## Risk Flags")
    for item in risk_flags:
        st.write(f"- {item}")

    st.markdown("## Priority Nursing Actions")
    for item in actions:
        st.write(f"- {item}")

    st.markdown("## Patient Education")
    for item in education:
        st.write(f"- {item}")

    st.markdown("## Why These Were Flagged")
    for item in reasons:
        st.write(f"- {item}")

    st.markdown("## Escalation Level")
    st.write(escalation)

st.markdown("---")
st.caption(
    "Disclaimer: This project is for educational purposes only. "
    "It does not diagnose, treat, or replace professional medical judgment."
)        
