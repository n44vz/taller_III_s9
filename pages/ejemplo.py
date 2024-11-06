import streamlit as st
import plotly.express as px 
import pandas as pd 

from utils.cargar_datos import cargar_datos

cargar_datos()


st.title("Ejemplo")

df = pd.DataFrame({
    'cuenta_total': [10, 20, 30, 40, 50],
    'tamano_mesa': [1, 2, 3, 4, 5]
}
)

st.dataframe(df)

mascara = df['cuenta_total'] > 10

st.write(mascara)

mascara1 = mascara & (df['tamano_mesa'] >= 3)

st.write(mascara1)
