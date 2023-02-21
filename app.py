import streamlit as st
import numpy as np
import pandas as pd
import plotly_express as px
import altair as alt
from st_vizzu import *
from streamlit_option_menu import option_menu
from streamlit_toggle import st_toggle_switch
from streamlit_extras.dataframe_explorer import dataframe_explorer
from ipyvizzu import Chart, Data, Config, Style

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
            columns = ['Posting type', 'Account entry description', 'Currency']
            bar_chart_df = data.filter(columns)
            st.bar_chart(bar_chart_df)
        
        with col_pai_chart:
            medal_type = st.selectbox('', ['Main account', 'Amount', 'Party name'])

            fig = px.pie(data, values=medal_type, names='Posting type',
                 title=f'number of {medal_type} medals',
                 height=300, width=200)
            fig.update_layout(margin=dict(l=20, r=20, t=30, b=0),)
            st.plotly_chart(fig, use_container_width=True)

        st.subheader("Data Grid")
        col_ipyv, col_grid_data = st.columns(2)

        with col_ipyv:
            # ipyv implementation
            # Load Data
            df = pd.read_excel("Dummy DataSet.xlsx")
            # Create ipyvizzu Object with the DataFrame
            obj = create_vizzu_obj(df)

            # Preset plot usage. Preset plots works directly with DataFrames.
            bar_obj = bar_chart(df,
                        x = "Posting type", 
                        y = "Amount",
                        title= "Using ipyvizzu`"
                        )

            # Animate with defined arguments 
            anim_obj = beta_vizzu_animate( bar_obj,
                x = "Voucher",
                y =  ["Amount", "Posting type"],
                title = "Animate with beta_vizzu_animate () function",
                label= "Popularity",
                color="Voucher",
                legend="color",
                sort="byValue",
                reverse=True,
                align="center",
                split=False,
            )

            # Animate with general dict based arguments 
            _dict = {"size": {"set": "Popularity"}, 
                "geometry": "circle",
                "coordSystem": "polar",
                "title": "Animate with vizzu_animate () function",
                }
            anim_obj2 = vizzu_animate(anim_obj,_dict)

            # Visualize within Streamlit
            with st.container(): # Maintaining the aspect ratio
                st.button("Animate")
                vizzu_plot(anim_obj2)
            # end of ipyv implementation

        with col_grid_data:
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