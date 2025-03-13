import re
import streamlit as st

# Page styling
st.set_page_config(page_title="Password Strength Meter", page_icon="🔒", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        .stTextInput > div > div > input {
            text-align: center; 
        }
        .stButton button {
            background-color: blue; 
            color: white; 
            font-size: 18px;
            width: 100%;
        }
        .stButton button:hover {
            background-color: red; 
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🔒 Password Strength Meter")
st.write("Enter your password to check its strength.")

# Check Password Strength function
def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least **8 characters long**.")

    # Uppercase and Lowercase
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **both uppercase and lowercase letters**.")

    # Number
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one number**.")

    # Special Character
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Password should have **at least one special character**.")

    # Password Strength Results
    if score == 4:
        st.success("✅ **Strong Password** - Your password is secure.")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - Consider improving your password by adding more security features.")
    else:
        st.error("❌ **Weak Password** - Follow the suggestions below to strengthen your password.")

    # Feedback
    if feedback:
        with st.expander("**Improve Your Password**"):
            for item in feedback:
                st.write(item)

# Creating a centered layout
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong")

    if st.button("Check Strength"):
        if password:
            check_password_strength(password)
        else:
            st.warning("⚠️ Please enter a password!")
