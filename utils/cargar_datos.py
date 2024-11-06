import plotly.express as px 
import streamlit as st 


def cargar_datos():
    df = px.data.tips()
    st.markdown('''

    ### Los datos se han cargado con éxito. :rocket:

    ''')
    
    
    