'''
Interacción con Gemini desde la terminal. 

(Generar API Key en https://aistudio.google.com)
'''


import requests

# Pega aqui tu API key (la que copiaste de Google AI Studio).
API_KEY = ""

MODEL = "gemini-3.6-flash"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

# A diferencia de PokeAPI, aqui la key no va en la URL: va en un header.
# Poner credenciales en la URL es mala practica (queda en logs, historial
# del navegador, etc.), asi que Gemini pide mandarla en un header aparte.
headers = {
    "Content-Type": "application/json",
    "x-goog-api-key": API_KEY,
}

# El "cuerpo" (body) de la peticion: aqui va el prompt.
# Fijate que ya no es una URL con datos pegados, es JSON de verdad.
body = {
    "contents": [
        {
            "parts": [
                {"text": "Desde cuando existe Pokemon?"}
            ]
        }
    ]
}

# Como el body no es un simple GET, usamos requests.post() y le pasamos
# el diccionario de Python directo en json=... (requests lo convierte
# a JSON por nosotros).
respuesta = requests.post(URL, headers=headers, json=body)

print("Status code:", respuesta.status_code)

if respuesta.status_code != 200:
    print("Algo salio mal:")
    print(respuesta.text)
else:
    datos = respuesta.json()

    # La respuesta de Gemini viene anidada varios niveles:
    # datos -> candidates -> [0] -> content -> parts -> [0] -> text
    texto = datos["candidates"][0]["content"]["parts"][0]["text"]
    print("\nRespuesta de Gemini:\n")
    print(texto)
