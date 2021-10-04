import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config( 
    page_title= 'Sales Dashboard',
    page_icon= ':bar_chart:',
    
)


df = pd.read_excel( 
        'https://github.com/Sven-Bo/streamlit-sales-dashboard/blob/main/supermarkt_sales.xlsx?raw=true',
        sheet_name='Sales',
        engine='openpyxl',
        skiprows=3,
        nrows=1000,
        usecols='B:R'

)
st.title('My first app')
st.write("Dapibus eget dictum magnis tristique orci odio leo suspendisse, netus natoque turpis accumsan sapien egestas iaculis. Porttitor curae mattis euismod senectus ante varius nullam natoque malesuada dictum, venenatis fringilla quam ultrices tempus sapien feugiat parturient et, imperdiet dictumst sagittis cubilia vehicula leo aptent dis velit. Taciti eget est tincidunt malesuada condimentum nunc aenean netus, posuere ad at felis leo ullamcorper sociis nostra tellus, lobortis etiam fringilla penatibus inceptos imperdiet iaculis.")

