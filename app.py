import streamlit as st
import pandas as pd
import plotly.express as px

data_vehicles=pd.read_csv('vehicles_us.csv')
data_vehicles.info()

#print(data_vehicles.duplicated().sum()) # verifica cuantas filas hay completamente repetidas

data_vehicles['model_year']=data_vehicles['model_year'].fillna('no_year')

data_vehicles['cylinders']=data_vehicles['cylinders'].fillna('0')

data_vehicles['date_posted']=pd.to_datetime(data_vehicles['date_posted'], format='%Y-%m-%d')
data_vehicles.info()

#fig = px.histogram(data_vehicles, x="odometer") # crear un histograma
#fig.show()

data_fuel=data_vehicles.groupby('fuel').count().reset_index()
#print(data_fuel)

#fig2=px.bar(data_fuel,x='fuel', y='price')
#fig2.show()

st.header('Análisis de datos de vehiculos registrados en U.S.A.')

st.write(st.session_state['data_vehicles'])

hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
     # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(data_vehicles, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

dis_button= st.button("Construir gráfico de dispersión ")

if dis_button:
    #escribir mensaje
    st.write("Creación de gráfico de dispersión para el precio del vehiculo vs. el kilometraje")

    fig2= px.scatter(data_vehicles, x='odometer', y='price')
    
    st.plotly_chart(fig2, use_container_width=True)