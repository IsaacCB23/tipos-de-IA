# tipos-de-IA
 IA general, IA clasica e IA generativa
# IA General: Asistente con NLTK

El asistente virtual utiliza la librería `nltk` para procesar las consultas del usuario y responder en función de las expresiones definidas. Además, integra una funcionalidad para consultar el clima en una localidad mexicana a través de la API de OpenWeatherMap y realizar cálculos matemáticos simples.

## Funciones principales:

- **Obtener clima**: Esta función permite al usuario consultar el clima en una localidad mexicana a partir de su código postal, proporcionando información como la temperatura, la sensación térmica, la humedad y la descripción del clima.
  
- **Cálculos matemáticos**: El asistente también puede realizar cálculos matemáticos simples, como sumas, restas, multiplicaciones y divisiones, a partir de expresiones ingresadas por el usuario.

---

# IA Clásica: Análisis de Música con Spotify

El código a continuación se conecta a la API de Spotify para buscar canciones populares de un artista o de un año específico. Los datos se leen desde un archivo CSV que contiene información de canciones populares.

## Funciones principales:

- **Conexión con Spotify**: Utiliza las credenciales de cliente de Spotify para autenticar y acceder a su API, lo que permite interactuar con los datos de música almacenados en la plataforma.

- **Procesamiento de datos musicales**: El asistente puede cargar un archivo CSV con información sobre canciones y realizar consultas sobre la popularidad de canciones de un artista o de un año específico.

---

# IA Generativa: Creación de Poesía con OpenAI

Esta parte del proyecto utiliza la API de OpenAI para generar poesía de acuerdo a un tema proporcionado por el usuario.

## Funciones principales:

- **Generación de poesía**: La función de generación de poesía toma un tema proporcionado por el usuario y utiliza el modelo de OpenAI para crear un poema único sobre ese tema.

---

# Cómo ejecutar

1. Clona este repositorio.
2. Asegúrate de tener todas las dependencias instaladas (`nltk`, `requests`, `spotipy`, `openai`).
3. Ejecuta el archivo Python correspondiente a cada funcionalidad.
