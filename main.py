from juego import partida_completa
from bandas import lista_bandas
from colores import *
def main():
    print(PURPURA + "¡UN,DOS, TRES..RESPONDA OTRA VEZ -  ROCK" + RESET)
    lista_bandas()
    total = partida_completa()
    print(DORADOESTANDAR + f"\n Tu puntuacion total es: {total}" + RESET)
if __name__ == "__main__":
    main()