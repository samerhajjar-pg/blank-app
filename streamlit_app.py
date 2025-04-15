import streamlit as st

client_id=st.secrets["id"]

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.button("Submit",)

st.file_uploader("Load spreadsheet",["xlsx","csv"])
