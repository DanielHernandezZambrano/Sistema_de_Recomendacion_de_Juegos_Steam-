from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pandas as pd

df_developer = pd.read_parquet("./datasets_endpoints/games_developer.parquet")
df_user_data = pd.read_parquet("./datasets_endpoints/user_data.parquet")
df_reviews = pd.read_parquet("./datasets_endpoints/user_reviews_sentiment.parquet")


def str_to_float(value):      # metodo para sumar solo los valores numericos
    try:                      # de la columna 'price'
        return float(value)
    except ValueError:
        return 0


app = FastAPI()

@app.get("/")
def message():
    return "Mi primera API"

@app.get("/developer/{desarrollador}", response_class=HTMLResponse)
def developer(desarrollador: str):
    df_dev = df_developer[df_developer["developer"] == desarrollador]

    df_agrupado = df_dev.groupby(["year"], as_index=False).agg({"item_id":"count"})
    df_agrupado = df_agrupado.rename(columns={"item_id":"Cantidad de Items"})

    #Agrupar por año y por si el item es free
    df_agrupado_free = df_dev[df_dev['price'] == 'free'].groupby(["year"], as_index=False).agg({"item_id":"count"})
    df_agrupado_free = df_agrupado_free.rename(columns={"item_id": "free_items"})

    #Combinar los resultados y calcular el porcentaje de items 'free' por año
    df_agrupado = pd.merge(df_agrupado, df_agrupado_free, on="year", how="left")
    df_agrupado['Contenido Free'] = round(df_agrupado['free_items'] / df_agrupado['Cantidad de Items'] * 100, 2).fillna(0)

    #Eliminamos free_items
    df_agrupado = df_agrupado.drop("free_items", axis=1)

    #Renombramos 'year' por 'Año'
    df_agrupado = df_agrupado.rename(columns={"year":"Año"})

    #Convertimos a html
    df_html = df_agrupado.to_html(index=False)
    return df_html

@app.get("/userdata/{user_id}")
def userdata(user_id: str):
    df_user = df_user_data[df_user_data["user_id"] == user_id]    #creo un df de solo el usuario buscado

    dinero_gastado = df_user['price'].apply(str_to_float).sum()   #aplicando el metodo para sumar todo el dinero gastado

    cantidad_items = len(df_user)                                 # obteniendo el verdadero valor de items (los que 'machean')

    df_reviews_user = df_reviews[df_reviews["user_id"] == user_id]   # un df de reviews para el usuario buscado
    total_reviews = len(df_reviews_user)                             # Obtenemos el total de reviews

    cantidad_true = df_reviews_user["recommend"].sum()               # Obtenemos el total de reviews de recommend que son True

    porcentaje_de_recomendacion = (cantidad_true * 100) / total_reviews # Obtenemos el porcentaje de recomendación

    respuesta = {"Usuario X": user_id, 
                 "Dinero gastado": dinero_gastado, 
                 "% de recomendación": round(porcentaje_de_recomendacion, 2), 
                 "cantidad de items": cantidad_items}
    
    return respuesta