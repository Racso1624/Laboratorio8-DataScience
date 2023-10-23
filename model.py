# Se cargan las librerias
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from sklearn.model_selection import train_test_split

# Se crea la clase del modelo
class PredictiveModel():

    # Se inicia el modelo
    def __init__(self) -> None:
        self.model = None
        self.createModel()

    # Funcion para crear el modelo
    def createModel(self):

        # Carga de datos
        df = pd.read_csv("data/houses_to_rent_v2.csv")

        # Tratar valores faltantes
        df = df.dropna()

        # Modificar las variables categoricas
        label_encoder = LabelEncoder()
        categoricas = ["city", "floor", "animal", "furniture"]
        for columna in categoricas:
            df[columna] = label_encoder.fit_transform(df[columna])

        # Dropear las variables para realizar la prediccion
        X = df.drop("total (R$)", axis=1)
        X = X.drop("hoa (R$)", axis=1)
        X = X.drop("rent amount (R$)", axis=1)
        X = X.drop("property tax (R$)", axis=1)
        X = X.drop("fire insurance (R$)", axis=1)
        y = df["total (R$)"]

        # Ajustar el modelo a los datos que se tienen
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        # Cargar el modelo en la clase
        self.model = model

    # Funcion para brindar el resultado de la prediccion
    def predict(self, city, area, rooms, bathrooms, parking, floors, pets, furniture):
        
        # Cargar la data
        user_data = [[city, area, rooms, bathrooms, parking, floors, pets, furniture]]
        # Retornar la prediccion
        return self.model.predict(user_data)[0]