import yfinance as yf
import streamlit as st
import datetime

stock = st.text_input('Input the name of the stock','GOOG')
data = yf.Ticker(stock)

st.header('Stock analysis app')
st.write("Currently analyzing",stock)

col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input('Enter the starting date', datetime.date(2024, 1, 1))
with col2:
    end_date = st.date_input('Enter the ending date', datetime.date(2024, 1, 31))

hist = data.history(period='1d',start='2019-01-01',end='2022-12-31')
st.write(hist)

st.subheader('Trend in closing pricing')
st.line_chart(hist['Close'])

st.subheader('Trend in volume')
st.bar_chart(hist['Volume'])