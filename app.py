# Laboratorio 8
# Integrantes:
# Oscar López (20679)
# Rodrigo Barrera (20807)

# Importar libreria
import streamlit as st
import matplotlib.pyplot as plt
from model import *

# Se carga el modelo de prediccion
predictive_model = PredictiveModel()

# Para los graficos
st.set_option('deprecation.showPyplotGlobalUse', False)

# Titulo de la pagina
st.title('Prediccion Precios de Alquiler')
st.subheader('Ingrese los siguientes datos:')

# Variables que contienen informacion del usuario
list_of_cities = ["Sao Paulo", "Campinas", "Belo Horizonte", "Porto Alegre", "Rio de Janeiro"]
city = st.selectbox("Seleccione la ciudad", list_of_cities)
city = list_of_cities.index(city)
area = st.number_input("Ingrese el área que desea:", min_value=1, max_value=500)
rooms = st.number_input("Ingrese la cantidad de cuartos que desea:", min_value=1, max_value=5)
bathrooms = st.number_input("Ingrese la cantidad de baños que desea:", min_value=1, max_value=5)
parking_spaces = st.number_input("Ingrese la cantidad de parqueos que desea:", min_value=1, max_value=5)
floors = st.number_input("Ingrese el piso que desea:", min_value=1, max_value=30)
pets = st.checkbox('Tiene mascotas?')
furniture = st.checkbox('Desea amueblado?')

# Boton para obtener prediccion
predict_button = st.button("Calcular el precio de Alquiler")

# Se realiza la prediccion del alquiler
if(predict_button):
    total_rent = predictive_model.predict(city, area, rooms, bathrooms, parking_spaces, floors, pets, furniture)
    st.success(f"El resultado de la renta total es: R${round(total_rent, 2)}")

# Seccion de greaficos
st.subheader("Sección Gráficos de Tendencias de Alquiler")
# Se toma la data
data = pd.read_csv("data/houses_to_rent_v2.csv")

# Total de renta por cada una de las ciudades
average_rent = data.groupby("city")["total (R$)"].mean()
average_rent.plot(kind="bar", figsize=(10, 6))
plt.title("Promedio de Renta Total en Ciudad")
plt.xlabel("Ciudad")
plt.ylabel("Promedio de Renta")
st.pyplot()

# Total de renta por la cantidad de cuartos
rooms_average = data.groupby("rooms")["total (R$)"].mean()
rooms_average.plot(kind="bar", figsize=(10, 6))
plt.title("Promedio de Total de Renta por Cuartos")
plt.xlabel("Cuartos")
plt.ylabel("Promedio de Renta")
st.pyplot()

# Total de area por la cantidad de cuartos
rooms_area_average = data.groupby("rooms")["area"].mean()
rooms_area_average.plot(kind="bar", figsize=(10, 6))
plt.title("Promedio de Total de Area por Cuartos")
plt.xlabel("Cuartos")
plt.ylabel("Promedio de Area")
st.pyplot()