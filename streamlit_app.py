import streamlit as st
import requests


st.title("Currency converter")

@st.cache_data
def get_currencies():
    response = requests.get('https://api.frankfurter.dev/v1/latest').json()
    return list(response['rates'].keys())

currencies = get_currencies()

amount = st.sidebar.number_input("Amount")
source_currency = st.sidebar.selectbox("Source currency",currencies)
target_curency = st.sidebar.multiselect("Target curency",currencies)
d = st.sidebar.date_input("Date")

calculate = st.sidebar.button("Convert", use_container_width=True)

if calculate:
    url = f"https://api.frankfurter.dev/v1/{d}?amount={amount}&from={source_currency}&to={','.join(target_curency)}"
    st.write(f"URL: {url}")

    response = requests.get(url)
    json = response.json()

    # st.write(json)


    for c in json['rates']:
        st.write(f"{json['rates'][c]} {c}")