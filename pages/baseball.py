import pandas as pd 
import streamlit as st
import plotly.express as px
import sqlite3
import os

carpeta = os.path.dirname(__file__) 

st.write('Esta es mi carpeta', carpeta)

db_path = os.path.join(carpeta, '..', 'data', 'lahman_1871-2022.sqlite')

a = 1
b = 2
c = 3

st.write(a, b ,c)

st.write('este es el db path:', db_path)

conn = sqlite3.connect(db_path)

st.write(conn)

people_query_df = pd.read_sql_query("SELECT * FROM People", conn)
st.dataframe(people_query_df)

tablas = pd.read_sql("SELECT name FROM sqlite_master WHERE type = 'table'", conn)

dataframes = {}

for tabla in tablas['name']:
    dataframes[tabla] = pd.read_sql(f"SELECT * FROM {tabla}", conn)
    
conn.close()   
    
AllstarFull = dataframes['AllstarFull']

st.dataframe(AllstarFull)



