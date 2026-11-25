#Aqui ponemos las bandas
# bandas.py
grupos = {
  "Queen": {"anio":1970,"cantante":"Freddy Mercuri"},
  "Foreigner":{"anio":1976, "cantante": "Lou Gram, Kelly Hansen"},
  "Bon Jovi":{"anio": 1983,"cantante": "Jon bon jovi"},
  "WhiteSnake":{"anio": 1981,"cantante": "David Coverdale"},
  "Metallica":{"anio": 1981, "cantante": "James Hetfield"},
  "Europe": {"anio":1979, "cantante": "Joey Tempest"},
  "Black Sabath" :{"anio": 1968, "cantante": "Ozzy Osbourne"},
  "Scorpion":{"anio": 1965, "cantante": "Klaus Meine"},
  "The Rolling Stones": {"anio": 1968, "cantante": "Mick Jagger"}
}
def lista_bandas():
    from colores import AMARILLOCLARO, RESET
    print(AMARILLOCLARO + f"\n Bandas del juego:" + RESET)
for nombre in grupos.keys():
    print(f".{nombre}")
    