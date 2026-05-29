import streamlit as st

st.write('Welcome to my app')

st.write(st.secrets['spell'])
key = st.secrets.some_magic_api.key
st.write(f"siteweb{key}")
