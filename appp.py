
import streamlit as st
with st.form(key='my_form'):
    st.write("merlix")
    username = st.text_input('Username')
    password = st.text_input('Password')
    if st.form_submit_button('Login'):
        print(username)
        print(password)

   