import streamlit as st



st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.button("Submit",)

st.file_uploader("Load spreadsheet",["xlsx","csv"])

st.write(st.secrets["id"])