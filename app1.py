import streamlit as st
import re

st.set_page_config(page_title="🔐 Password Strength Meter", layout="centered")

# Custom CSS for beautification
st.markdown("""
<style>
.stApp {
    background-color: #f5f7fa;
    color: #333;
    font-family: 'Segoe UI', sans-serif;
}
.Password-title {
    font-size: 36px;
    font-weight: bold;
    color: #2c3e50;
    text-align: center;
    margin-bottom: 20px;
}
.tip {
    font-size: 18px;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<div class='Password-title'>🔐 Password Strength Checker 🔍</div>", unsafe_allow_html=True)
st.write("Welcome! 😊 This tool helps you craft **strong secure password**. Type password below to check its strength and get tips to improve it. Your digital safety matters! 🔐💪")

# User input
password = st.text_input("🔑 Enter your password:", type="password")

def check_strength(password):
    score = 0
    remarks = []

    if len(password) >= 8:
        score += 1
    else:
        remarks.append("🔸 Use at least 8 characters.")

    if re.search(r"\d", password):
        score += 1
    else:
        remarks.append("🔸 Add a number like 123.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        remarks.append("🔸 Use both UPPER and lower case letters (Aa).")

    if re.search(r"[!@#$%^&*(),.?\":{|<>}]", password):
        score += 1
    else:
        remarks.append("🔸 Include special characters (!@#$ etc).")

    return score, remarks


# Display output
if password:
    score, feedback = check_strength(password)

    if score <= 1:
        strength = "Weak 😕"
        color = "red"
    elif score == 2 or score == 3:
        strength = "Medium 🙂"
        color = "orange"
    else:
        strength = "Strong 💪"
        color = "green"

    st.markdown(f"<h3 style='color:{color}'>Password Strength: {strength}</h3>", unsafe_allow_html=True)

    st.progress(score * 25)

    if feedback:
        st.markdown("**🛠 Suggestions to improve your password:**")
        for suggestion in feedback:
            st.write(suggestion)
else:
    st.info("🔍 Start typing a password to see the strength analysis.")

# Footer
st.markdown("---")
st.write("🧠 **Tip:** Use a mix of characters and avoid using names or birthdays.")
st.write("🌟 Created with 💻 by **Sanoober** – Stay safe out there! 🔒")
