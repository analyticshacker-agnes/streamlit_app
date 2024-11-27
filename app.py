import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# App Title
st.title("Google Search Console Data Analysis")

# File Upload
uploaded_file = st.file_uploader("Upload your Google Search Console CSV file", type=["csv"])

if uploaded_file:
    # Load Data
    data = pd.read_csv(uploaded_file)

    # Display Raw Data
    st.subheader("Raw Data")
    st.dataframe(data)

    # Metrics Overview
    st.subheader("Performance Overview")
    total_clicks = data['Clicks'].sum()
    total_impressions = data['Impressions'].sum()
    avg_ctr = total_clicks / total_impressions * 100
    avg_position = data['Position'].mean()

    st.metric("Total Clicks", total_clicks)
    st.metric("Total Impressions", total_impressions)
    st.metric("Average CTR (%)", round(avg_ctr, 2))
    st.metric("Average Position", round(avg_position, 2))

    # Top Keywords by Clicks
    st.subheader("Top Keywords by Clicks")
    top_keywords = data[['Query', 'Clicks']].sort_values(by='Clicks', ascending=False).head(10)
    st.bar_chart(top_keywords.set_index('Query'))

    # CTR vs Position Scatter Plot
    st.subheader("CTR vs Position")
    fig = px.scatter(data, x="Position", y="CTR", size="Impressions", color="Query",
                     title="CTR vs Average Position", labels={"CTR": "Click-Through Rate (%)"})
    st.plotly_chart(fig)

    # Recommendations
    st.subheader("Recommendations")
    st.write("""
    - Improve CTR for high-impression, low-CTR keywords.
    - Optimize content for keywords ranking in positions 11-20.
    - Focus on increasing relevance for underperforming pages.
    """)

else:
    st.info("Awaiting CSV file upload. Please upload your Google Search Console data.")
