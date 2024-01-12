import streamlit as st
import pandas as pd

from src.functions import load_data,get_summary,plot_sales_over_time


def main():
    st.title('Supermarket Sales Dashboard')
 
    data = load_data()
    st.sidebar.header('Controls')
    min_rating = st.sidebar.slider('Minimum Rating', min_value=0, max_value=10, value=5, step=1)
    
    filtered_data = data.loc[data['Rating']>=min_rating]
    summary = get_summary(filtered_data)
    
    # Display summary stats
    st.write("### Summary Statistics")
    st.table(summary)
    
    # Display raw data
    st.write("### Raw Data")
    st.dataframe(filtered_data)
    
    # Plotting
    st.write("### Sales Over Time")
    st.pyplot(plot_sales_over_time(filtered_data))


if __name__ == '__main__':
    main()

