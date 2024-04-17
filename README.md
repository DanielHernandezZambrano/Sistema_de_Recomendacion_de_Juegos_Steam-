# <center> **Sistema de Recomendación de Juegos para la Plataforma Steam** </center>

![Logo](./datasets_endpoints/machine_learning_746x419.jpg)


Este proyecto tiene como objetivo desarrollar un motor de recomendación de juegos utilizando datos proporcionados por la reconocida plataforma de videojuegos, Steam. La meta es ofrecer a los usuarios recomendaciones precisas y personalizadas basadas en sus preferencias de juego, además de proporcionar información de la plataforma habilitada en nuestra API.

### Descripción del Proyecto

Adentrarse en el papel de Científico de Datos en Steam, una de las principales plataformas multinacionales de videojuegos, es un viaje emocionante al mundo del análisis de datos. Sin embargo, el entusiasmo inicial se enfrenta de inmediato a la cruda realidad: la necesidad urgente de crear un sistema de recomendación de videojuegos para los usuarios de Steam. Al explorar los datos disponibles, se encuentra con un desafío considerable: la falta de madurez de los mismos, con estructuras anidadas y carentes de formato definido. Además, la ausencia total de procesos automatizados para la actualización de nuevos productos.

## Objetivos

Como *Científico de Datos*, el objetivo principal es abordar el complejo desafío de desarrollar un sistema de recomendación de videojuegos centrado en el usuario. Esto implica:

1. Crear un sistema de recomendación de videojuegos basado en datos para Steam, incorporando una API fácil de usar con FastAPI para un acceso fluido a sugerencias personalizadas.
2. Realizar un Análisis Exploratorio de Datos (EDA) y entrenar un modelo de aprendizaje automático, centrándose en aprovechar algoritmos de similitud de juegos avanzados para obtener recomendaciones personalizadas *(similitud del coseno)*.

## **Funcionalidad de la API**

Se utilizó el framework FastAPI para desarrollar una API que ofrece puntos finales específicos:

- def developer( desarrollador : str ): Devuelve la cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora.

- def userdata (User_id : str): Devuelve cantidad de dinero gastado por el usuario, el porcentaje de recomendación en base a reviews y cantidad de items.

- def UserForGenre( genero : str ): Devuelve el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.

- def best_developer_year( año : int ): Devuelve el top 3 de desarrolladores con juegos más recomendados por usuarios para el año dado.

- def developer_reviews_analysis( desarrolladora : str ): Devuelve un diccionario con el nombre del desarrollador como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor positivo o negativo.

## **Aprendizaje Automático**

El punto final de este proyecto es el modelo de aprendizaje automático: 

- def recomendacion_juego( id de producto ): Ingresando el id de producto, recibes una lista con 5 juegos recomendados similares al ingresado.