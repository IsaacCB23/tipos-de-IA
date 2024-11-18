# -*- coding: utf-8 -*-
"""IAGenerativa

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xGoNZSxgXG4O9aoW9_IZZ0wH9kf6lt9P
"""

!pip install openai

from openai import OpenAI

#API key de OpenAI
client = OpenAI(api_key='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')

# generar poesía según el tema elegido por el usuario
def generar_poesia(tema):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un asistente creativo."},
            {"role": "user", "content": f"Escribe un poema acerca de: {tema}."}
        ],
        temperature=1,  # controla la creatividad de la respuesta
        max_tokens=150,  # número de palabras que queremos generar
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        response_format="text"  # el formato de respuesta será texto
    )

    # extraemos y retornamos la poesía generada
    poesia = response['choices'][0]['message']['content'].strip()
    return poesia

# solicitar al usuario un tema para la poesía
tema = input("Por favor, elija un tema para el poema: ")
poesia = generar_poesia(tema)

# mostrar la poesía generada
print("\nPoesía Generada:\n")
print(poesia)