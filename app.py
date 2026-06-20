import streamlit as st

CLIENT_ID = "494634548519-5ipea5s13rgveneuov867tubbc60qsou.apps.googleusercontent.com"

phone = st.query_params.get("phone", "")

redirect_uri = "https://connect.airaofficial.my.id"

auth_url = (
    "https://accounts.google.com/o/oauth2/v2/auth"
    f"?client_id={CLIENT_ID}"
    "&response_type=code"
    "&scope=https://www.googleapis.com/auth/calendar"
    "&access_type=offline"
    "&prompt=consent"
    f"&redirect_uri={redirect_uri}"
    f"&state={phone}"
)

st.title("AIRA Google Calendar")

st.write("Hubungkan Google Calendar Anda")

st.link_button(
    "Connect Google Calendar",
    auth_url
)
