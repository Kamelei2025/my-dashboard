import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# 1. Page Configuration
st.set_page_config(page_title="My Interactive Dashboard", layout="wide")

# 2. Data Source
@st.cache_data
def load_data():
    dates = pd.date_range(start='2024-01-01', periods=100, freq='D')
    df = pd.DataFrame({
        'Date': dates,
        'Metric_A': np.random.randint(10, 100, size=100),
        'Metric_B': np.random.randint(50, 200, size=100),
        'Category': np.random.choice(['Mobile', 'Web', 'Desktop'], size=100)
    })
    return df

df = load_data()

# 3. Sidebar Filters
st.sidebar.header("Dashboard Filters")
category_filter = st.sidebar.multiselect(
    "Filter by Category:",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

filtered_df = df[df["Category"].isin(category_filter)]

# 4. Header Section
st.title("🚀 My Interactive Analytics Dashboard")

# 5. KPI Metrics Row
col1, col2, col3 = st.columns(3)
col1.metric("Total Metric A", f"{filtered_df['Metric_A'].sum()}")
col2.metric("Avg Metric B", f"{int(filtered_df['Metric_B'].mean())}")
col3.metric("Data Points", f"{len(filtered_df)}")

st.divider()

# 6. Charts Row
left_chart, right_chart = st.columns(2)

with left_chart:
    st.subheader("Performance Trend")
    fig_line = px.line(filtered_df, x="Date", y="Metric_A", color="Category", markers=True)
    st.plotly_chart(fig_line, use_container_width=True)

with right_chart:
    st.subheader("Category Distribution")
    fig_bar = px.bar(filtered_df, x="Category", y="Metric_B", color="Category")
    st.plotly_chart(fig_bar, use_container_width=True)
