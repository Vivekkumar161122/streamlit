import streamlit as st

st.title("My First Streamlit App")
name = st.text_input("Enter your name:")
if name:
  st.write(f"Hello, {name}!")


''' 
To run this type the command "streamlit run enter-your-name.py" and to close the streamlit click in the terminal command ans then ctrl + C
''' 

