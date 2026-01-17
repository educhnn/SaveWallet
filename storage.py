import json

def guardar_gastos(gastos):
    with open("gastos.json", "w")as archivo:
        json.dump(gastos, archivo)

def cargar_gastos():
    try:
        with open("gastos.json","r")as archivo:
            gastos = json.load(archivo)
            return gastos
    except FileNotFoundError:
        gastos = []
        return gastos