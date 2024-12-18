# -*- coding: utf-8 -*-
"""IAClasica

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1a_6Sw5nE6qobiRS0719DoyIrwS14tseq
"""

!pip install spotipy

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# configura las credenciales de la API de Spotify
CLIENT_ID = 'a9c590eeb5eb419f9c19b2c81d401365'
CLIENT_SECRET = 'a01516eea9a94c4591eb90c7e77e6726'

# autenticación con la API de Spotify
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# cargar el dataset en un DataFrame
file_path = '/content/drive/MyDrive/FIA/spotify_data (1).csv'
spotify_data = pd.read_csv(file_path)

# copiar el dataset para filtrar sin modificar el original
spotify_data_copy = spotify_data.copy()

# limpiar columnas en caso de valores nulos
spotify_data_copy = spotify_data_copy.dropna(subset=['artist_name', 'year'])

# obtener el enlace de Spotify de una canción
def obtener_enlace_spotify(artista, cancion):
    result = sp.search(q=f"track:{cancion} artist:{artista}", type="track", limit=1)

    if result['tracks']['items']:
        return result['tracks']['items'][0]['external_urls']['spotify']
    else:
        return None

# mostrar el top 10 de canciones populares de un artista
def buscar_canciones_artista(artista):
    if not artista:  # Si no se ingresa ningún nombre de artista
        print("Por favor, ingrese un nombre de artista válido.")
        return

    # filtrar el dataset por el nombre del artista (ignorando mayúsculas/minúsculas)
    filtro = spotify_data_copy[spotify_data_copy['artist_name'].str.contains(artista, case=False, na=False)]

    if filtro.empty:
        print(f"No se encontraron canciones de {artista}. Intenta con otro nombre.")
    else:
        # mostrar las canciones más populares (top 10)
        top_10 = filtro.sort_values(by='popularity', ascending=False).head(10)
        print("Top 10 canciones populares de", artista)
        for index, row in top_10.iterrows():
            cancion = row['track_name']
            artista = row['artist_name']
            url_spotify = obtener_enlace_spotify(artista, cancion)
            if url_spotify:
                print(f"{cancion} - {artista}: {url_spotify}")
            else:
                print(f"{cancion} - {artista}: No encontrado en Spotify")

# mostrar el top 10 de canciones populares de un año específico
def buscar_canciones_por_ano(ano):
    if not ano.isdigit() or int(ano) < 1900 or int(ano) > 2024:  # Asegurarse de que el año es válido
        print("Por favor, ingrese un año válido.")
        return

    # filtrar el dataset por el año
    filtro = spotify_data_copy[spotify_data_copy['year'] == int(ano)]

    if filtro.empty:
        print(f"No se encontraron canciones del año {ano}. Intenta con otro año.")
    else:
        # mostrar las canciones más populares (top 10) del año específico
        top_10 = filtro.sort_values(by='popularity', ascending=False).head(10)
        print(f"Top 10 canciones populares del año {ano}")
        for index, row in top_10.iterrows():
            cancion = row['track_name']
            artista = row['artist_name']
            url_spotify = obtener_enlace_spotify(artista, cancion)
            if url_spotify:
                print(f"{cancion} - {artista}: {url_spotify}")
            else:
                print(f"{cancion} - {artista}: No encontrado en Spotify")

# mostrar opciones
def mostrar_top_10():
    while True:
        print("\n¿Qué deseas buscar?")
        print("1. Canciones populares de un artista.")
        print("2. Canciones populares de un año específico.")
        print("3. Salir.")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            artista = input("Ingresa el nombre del artista: ")
            buscar_canciones_artista(artista)
        elif opcion == '2':
            ano = input("Ingresa el año para buscar canciones populares: ")
            buscar_canciones_por_ano(ano)
        elif opcion == '3':
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

# ejecutar la función principal
mostrar_top_10()

