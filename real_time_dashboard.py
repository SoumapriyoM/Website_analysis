import streamlit as st
import pandas as pd
import plotly.express as px

def display_real_time_data(data):
    fig_line = px.line(data, x='Month', y=['Page_Load_Time', 'Bounce_Rate', 'Conversion_Rate'], 
                       title='Website Performance Metrics Over Time', labels={'value': 'Metric'})
    fig_bar = px.bar(data, x='Month', y=['Page_Load_Time', 'Bounce_Rate', 'Conversion_Rate'], 
                     title='Website Performance Metrics Comparison', labels={'value': 'Metric'},
                     barmode='group')
    st.plotly_chart(fig_line, use_container_width=True)
    st.plotly_chart(fig_bar, use_container_width=True)

data = pd.read_csv("website_performance.csv")

st.title("Real-Time Dashboard")
display_real_time_data(data)
