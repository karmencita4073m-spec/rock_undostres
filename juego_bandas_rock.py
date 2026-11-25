import random

from bandas import grupos
from colores import *


def jugar_ronda():
    lista_nombres = list(grupos.keys())
    nombre_aleatorio = random.choice(lista_nombres)
    info = grupos[nombre_aleatorio]
    tipo_pista = random.choice(("anio", "cantante"))

    if tipo_pista == "anio":
        print(MORADO + f"\nSe formó en el año {info['anio']} - ¿Qué banda es?" + RESET)
    else:
        print(AZULCLARO + f"\nSu cantante principal es {info['cantante']} - ¿Qué banda es?" + RESET)

    respuesta = input("Tu respuesta: ")

    if respuesta.strip().lower() == nombre_aleatorio.lower():
        print(VERDE + "¡Bingo! Acertaste. +1 punto" + RESET)
        return 1

    print(ROJOCLARO + f"¡Error! Es: {nombre_aleatorio}" + RESET)
    return 0


def partida_completa(num_rondas=5):
    puntuacion = 0
    print(BLANCOBRILLANTE + f"\nEmpezamos {num_rondas} rondas..." + RESET)

    for i in range(num_rondas):
        print(ROSA + f"\n--- Ronda {i + 1} ---" + RESET)
        puntuacion += jugar_ronda()

    print(BLANCOBRILLANTE + f"\nPuntuación final: {puntuacion}/{num_rondas}" + RESET)
    return puntuacion