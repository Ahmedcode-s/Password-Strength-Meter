import re
import streamlit as st

#styling
st.set_page_config(page_title="Password Strength Meter", page_icon="🔒" , layout="centered")

#css styling

st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {width:60% !important; margin:auto; }
    .stButton button {width: 50%; background-color: blue; color: white; font-size: 18px; }
    .stButton button:hover { background-color: red; color: white;}
<style>
""", unsafe_allow_html=True)

#Title
st.title("🔒 Password Strength Meter")
st.write("Enter your password to check its strength.")

#Check Password Strength function
def check_password_strength(password):
    score = 0
    feedback = []
#length

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be atleast **8 characters long**.")

#LowerCase and UpperCase
    if re.search(r"[A-Z]", password ) and re.search(r"[a-z]" , password):
        score += 1
    else:
        feedback.append("❌ Password should include **both UpperCase and LowerCase letters**.")
#Number
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include **atleast one Number**.")
#Special Character
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Password Should have **altest one special character**.")
#Password Strength results
    if score == 4:
        st.success("**Strong Password** Your password is secure")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - Consider improving your password by adding more security features ")
    else:
        st.error("❌ **Weak Password** - Follow the suggestion below to strengthen your password. ")

#feedback
    if feedback:
        with st.expander("**Improve Your Password**"):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong")

#Button 
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password!")
