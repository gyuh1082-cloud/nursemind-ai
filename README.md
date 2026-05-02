# NurseMind AI 🩺  
A Rule-Based Clinical Decision Support System for Nursing Risk Assessment

---

## Overview
NurseMind AI is a student-built clinical reasoning simulation designed to model how nurses assess patient risk, prioritize care, and respond to safety concerns.

Instead of using generative AI, it uses a rule-based decision engine to simulate structured nursing judgment in patient triage scenarios.

---

## Motivation
As a student interested in becoming a Nurse Practitioner, I built this project to simulate the analytical side of nursing.

Nurses constantly:
- Identify early warning signs
- Prioritize multiple patient risks
- Make fast safety-critical decisions

This project translates that process into a computational system.

---

## System Design

### Input Layer
- Patient age  
- Symptoms  
- Vital signs (blood pressure, temperature, oxygen level)  
- Medications  

### Processing Layer
- Rule-based conditional logic (if-statements)
- Clinical threshold evaluation
- Weighted severity scoring system
- Escalation logic (Low → Moderate → High)

### Output Layer
- Risk flags  
- Priority nursing actions  
- Monitoring instructions  
- Patient education  
- Clinical reasoning explanations  

---

## Key Features
- Detects patient safety risks in real time  
- Simulates nursing triage decision-making  
- Generates explainable clinical reasoning  
- Uses severity scoring for prioritization  
- Escalates high-risk cases automatically  

---

## Example Risks Detected
- Fall risk  
- Low blood pressure (hypotension)  
- Respiratory distress  
- Possible infection  
- Dehydration risk  
- Medication side effects  
- Acute mental status changes  

---

## Technical Decisions
- **Rule-Based System:** Ensures deterministic and explainable outputs  
- **Severity Scoring:** Assigns weighted values to clinical risk factors  
- **Escalation Logic:** Overrides normal scoring for critical symptoms  
- **Structured Outputs:** Separates actions, monitoring, and education  

---

## Limitations
- Not a medical diagnostic tool  
- Cannot capture full clinical complexity  
- No real patient data used  
- Does not integrate with hospital systems (EHR)  
- Edge cases may not be fully represented  

---

## Future Improvements
- Integration with synthetic clinical datasets  
- Hybrid AI + rule-based decision system  
- User testing with nursing students  
- Expanded triage scoring models  
- Improved real-time simulation interface  
- Hospital workflow simulation features  

---

## Tools Used
- Python  
- Streamlit  
- GitHub  

---

## Why This Project Matters
This project demonstrates that nursing is both compassionate and highly analytical. It translates real-world clinical reasoning into a structured computational system that prioritizes safety, clarity, and decision-making.

---

## Disclaimer
This project is for educational purposes only. It does not diagnose, treat, or replace professional medical judgment.
