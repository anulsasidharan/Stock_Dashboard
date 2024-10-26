import streamlit as st
import pandas as pd
import plotly_express as px
from datashader.datashape import numeric
from intake.source.utils import unique_string


@st.cache_data
def load_data():
    """Utility function"""
    df = pd.read_csv('Data/all_stocks_5yr.csv', index_col='date')

    numeric_df = df.select_dtypes(['float', 'int'])
    numeric_cols = numeric_df.columns

    text_df = df.select_dtypes(['object'])
    text_columns = text_df.columns

    stock_columns = df['Name']
    unique_stocks = stock_columns.unique()

    return df, numeric_cols, text_columns, unique_stocks


df, numeric_cols, text_columns, unique_stocks = load_data()
# st.write(numeric_cols)
st.title("Stocks Dashboard")

# Add a check box in the sidebar

check_box = st.sidebar.checkbox(label="Display the dataset")

# print(check_box)
if check_box:
    st.write(df)

# Title for sidebar
st.sidebar.title("Settings")
# Add a subheader
st.sidebar.subheader("TimeSeries Settings")

# Multi select widgets
feature_selection = st.sidebar.multiselect(label="Features to plot", options=numeric_cols)

# Add a select box for stock tickers
stock_ticker = st.sidebar.selectbox(label="Stock Ticker", options=unique_stocks)

print(feature_selection)
print(stock_ticker)