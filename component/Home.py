import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)

authenticator.login()


if st.session_state["authentication_status"]:
    authenticator.logout(button_name="Logout", location="sidebar")
    st.subheader(f'Welcome, *{st.session_state["name"]}*')
    st.write('Congratulations for being part of Generasi Hamid')
    st.image('images/welcome.png', use_column_width='always') 

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')

elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')