import streamlit as st
import numpy as np
import pandas as pd
from streamlit_option_menu import option_menu
from streamlit_toggle import st_toggle_switch
from streamlit_extras.dataframe_explorer import dataframe_explorer

st.set_page_config(layout="wide")

# Hide streamlit default menu and footer from the template
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden}
    footer {visibility: hidden}
    header {visibility: hidden}
    div.block-container {padding-top:1rem;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

data = pd.read_excel("Dummy DataSet.xlsx")

st.header('Financial Analysis')

# Tab as page
tab_dashboard, tab_raw_data, tab3 = st.tabs(["📈 Page1", "🗃 Page2", "🗃 Page3"])
with st.container():
    with st.sidebar:
        st.subheader("Filter with metrix")
        #nav_option = st.sidebar.radio("", ["Home", "Predection", "Contribute"])
        #nav_option_toggle = st.write("Enable options")
        nav_tog_op_1 = st_toggle_switch(
            label="Item 1",
            key="switch_1",
            default_value=False,
            label_after=False,
            inactive_color="#D3D3D3",  # optional
            active_color="#11567f",  # optional
            track_color="#29B5E8",  # optional
        )
        nav_tog_op_2 = st_toggle_switch(
            label="Item 2",
            key="switch_2",
            default_value=False,
            label_after=False,
            inactive_color="#D3D3D3",  # optional
            active_color="#11567f",  # optional
            track_color="#29B5E8",  # optional
        )
        nav_tog_op_3 = st_toggle_switch(
            label="Item 3",
            key="switch_3",
            default_value=False,
            label_after=False,
            inactive_color="#D3D3D3",  # optional
            active_color="#11567f",  # optional
            track_color="#29B5E8",  # optional
        )
        nav_tog_op_4 = st_toggle_switch(
            label="Item 4",
            key="switch_4",
            default_value=False,
            label_after=False,
            inactive_color="#D3D3D3",  # optional
            active_color="#11567f",  # optional
            track_color="#29B5E8",  # optional
        )
        nav_tog_op_5 = st_toggle_switch(
            label="Item 5",
            key="switch_6",
            default_value=False,
            label_after=False,
            inactive_color="#D3D3D3",  # optional
            active_color="#11567f",  # optional
            track_color="#29B5E8",  # optional
        )
    
    with tab_dashboard:
        st.subheader("Summary")
        col_barChart, col_pai_chart = st.columns(2)

        with col_barChart:
            st.write("This is Barchart")
            st.success("Here Bar chart will be placeed")
        
        with col_pai_chart:
            st.write("This is Pie Chart")
            st.success("Here pie chart will be placeed")

        st.subheader("Data Grid")
        columns = ['Journal number', 'Date', 'Voucher', 'Posting type', 'Account entry description', 'Main account', 'Main account name', 'Amount', 'Amount in transaction currency', 'Currency', 'Party name']
        new_df = data.filter(columns)
        filtered_df = dataframe_explorer(new_df)
        st.dataframe(new_df, use_container_width=True)

    with tab_raw_data:
        st.subheader("Raw data")
        st.dataframe(data)
    
        @st.cache_data
        def convert_df(data):
            return data.to_csv().encode('utf-8')
        
        csv = convert_df(data)

        st.download_button(
            label="Download as CSV",
            data=csv,
            file_name='raw.csv',
            mime='text/csv',
        )

    with tab3:
        st.subheader("For page 3")
        st.success("Page3 data analysis will be place here")