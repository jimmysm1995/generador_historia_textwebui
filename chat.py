import requests
import json

url = 'http://127.0.0.1:5000/v1/completions'
headers = {"Content-Type" : 'application/json'}

def get_temperature():
    print("Seleccione el nivel de creatividad:")
    print("a) Creatividad alta")
    print("b) Creatividad media")
    print("c) Creatividad baja")
    choice = input("Ingrese su elección (a/b/c): ").strip().lower()
    if choice == 'a':
        return 0.9
    elif choice == 'b':
        return 0.5
    elif choice == 'c':
        return 0.2
    else:
        print("Opción no válida, se usará creatividad media por defecto.")
        return 0.5

def get_max_tokens():
    print("Seleccione la longitud del texto:")
    print("a) Corto")
    print("b) Medio")
    print("c) Largo")
    choice = input("Ingrese su elección (a/b/c): ").strip().lower()
    if choice == 'a':
        return 100
    elif choice == 'b':
        return 200
    elif choice == 'c':
        return 300
    else:
        print("Opción no válida, se usará longitud media por defecto.")
        return 200

def get_top_p():
    print("Seleccione un valor para aumentar la diversidad del texto generado:")
    print("a) 0.9 (Alta diversidad)")
    print("b) 0.7 (Diversidad media)")
    print("c) 0.5 (Baja diversidad)")
    choice = input("Ingrese su elección (a/b/c): ").strip().lower()
    if choice == 'a':
        return 0.9
    elif choice == 'b':
        return 0.7
    elif choice == 'c':
        return 0.5
    else:
        print("Opción no válida, se usará diversidad media por defecto.")
        return 0.7

def get_frequency_penalty():
    print("Seleccione un valor para penalizar la repetición de palabras:")
    print("a) 0.0 (Sin penalización)")
    print("b) 0.5 (Penalización media)")
    print("c) 1.0 (Alta penalización)")
    choice = input("Ingrese su elección (a/b/c): ").strip().lower()
    if choice == 'a':
        return 0.0
    elif choice == 'b':
        return 0.5
    elif choice == 'c':
        return 1.0
    else:
        print("Opción no válida, se usará penalización media por defecto.")
        return 0.5

while True:
    main_character = input("Introduzca el nombre del personaje principal: ")
    second_character = input("Introduzca el nombre del personaje secundario: ")
    place = input("Introduzca el lugar donde transcurrirá la historia: ")
    action = input("Introduzca una acción importante que acontecerá en la historia: ")

    user_message = f"Crea una historia en {place}, en la que {main_character} es el personaje principal y {second_character} es el secundario, y ocurre {action}"

    temperature = get_temperature()
    max_tokens = get_max_tokens()
    top_p = get_top_p()
    frequency_penalty = get_frequency_penalty()

    body = {
        "prompt": user_message,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "top_p": top_p,
        "frequency_penalty": frequency_penalty
    }

    response = requests.post(url=url , headers=headers, json=body)
    mesagge = json.loads(response.content.decode('utf-8'))
    assistant_message = mesagge['choices'][0]['text']
    print(assistant_message)