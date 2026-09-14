'''
Interacción con Gemini desde la terminal. 

(Generar API Key en https://aistudio.google.com)
'''

from api_key import API_KEY
import requests


# CONSTANTES
VERBOSE = False
MODEL = 'gemini-3.6-flash'
URL = f'https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent'

# Print de configuración API
if VERBOSE:
    print(f'\n======================================')
    print(f'GEMINI MODEL: {MODEL}')
    print(f'API KEY: {API_KEY}')
    print(f'======================================\n')

# Construir header con API KEY
headers = {
    'Content-Type': 'application/json',
    'x-goog-api-key': API_KEY,
}

# ------ Arriba: constante | Abajo: dinámico o variante.

# Ciclo interactivo con gemini
while True:

    print(f'\n============== GEMINI ===============')

    user_prompt = input('En qué piensas? (ingresa tu prompr o "salir" para terminar la sesión): ')

    # Revisa si el usuario desea salir
    if user_prompt.lower().strip() == 'salir':
        print('\n Hasta luego!')
        break
    
    # Construir body de request
    body = {
        'contents': [
            {
                'parts': [
                    {'text': user_prompt}
                ]
            }
        ]
    }

    # Realizar request POST
    respuesta = requests.post(URL, headers=headers, json=body)

    if VERBOSE:
        print('Status code:', respuesta.status_code)

    if respuesta.status_code != 200:
        print('\nAlgo salio mal:')
        print(respuesta.text)
    else:
        datos = respuesta.json()
        # datos -> candidates -> [0] -> content -> parts -> [0] -> text
        respuesta_gemini = datos['candidates'][0]['content']['parts'][0]['text']
        print('\nRespuesta de Gemini:\n')
        print(respuesta_gemini)
