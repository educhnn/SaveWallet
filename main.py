import os
import json

gastos = []

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def guardar_gastos():
    with open("gastos.json", "w")as archivo:
        json.dump(gastos, archivo)

def cargar_gastos():
    global gastos
    try:
        with open("gastos.json","r")as archivo:
            gastos = json.load(archivo)
    except FileNotFoundError:
        gastos = []

def agregar_gasto():
    limpiar_pantalla()
    try:
        monto = float(input("Indique cuanto fue su gasto: "))
        categoria = input("Seleccione la categoria: ").lower()
        gasto = {
            "monto": monto,
            "categoria": categoria
        }
        gastos.append(gasto)
        guardar_gastos()
    except ValueError:
        limpiar_pantalla()
        input("INDIQUE UNICAMENTE NUMEROS")
        return

def mostrar_gastos():
    limpiar_pantalla()
    print("\tGASTOS")
    for gasto in gastos:
        print(f"{gasto['categoria']} - ${gasto['monto']}")
    input("Presiona enter para continuar...")

def mostrar_total():
    total = 0
    limpiar_pantalla()
    print("\tTOTAL DE GASTOS")
    for gasto in gastos:
        total += gasto["monto"] 
    print(f"Usted gastó un total de: ${total}")
    input("Presione enter para continuar...")

def filtrar():
    limpiar_pantalla()
    filtro = input("Ingrese la categoria: ").lower()
    limpiar_pantalla()
    print("\tFILTRO")
    encontrado = False

    for gasto in gastos:
        if gasto["categoria"] == filtro:
           print(f"{gasto['categoria']} - ${gasto['monto']}")
           encontrado = True
        
    if not encontrado:
        print("LA CATEGORIA NO EXISTE")

    input("Presione enter para continuar...")

def borrar_gastos():
    global gastos
    limpiar_pantalla()
    print("\tBORRAR GASTOS")
    if gastos:
        for i, gasto in enumerate(gastos):
            print(f"{i+1}) {gasto['categoria']} - ${gasto['monto']}")
        try:
            opcion = int(input("Seleccione el gasto que desea borrar: "))
            gastos.pop(opcion-1)
            guardar_gastos()
        except IndexError:
            limpiar_pantalla()
            input("EL GASTO ES INVALIDO PRESIONE ENTER PARA CONTINUAR...")
        except ValueError:
            limpiar_pantalla()
            input("INTRODUCE UNICAMENTE VALORES NUMERICOS PRESIONA ENTER PARA CONTINUAR...")
    else:
        input("No existen gastos actualmente, presione enter para continuar...")

def exportar_csv():
    limpiar_pantalla()
    if not gastos:
        input("No existen gastos actualmente, presione enter para continuar...")
        return
    try:
        with open("gastos.csv", "w",encoding="utf-8")as archivo:
            archivo.write("categoria,monto\n")
            for gasto in gastos:
                archivo.write(f"{gasto['categoria']},{gasto['monto']}\n")
            input("Archivo creado correctamente...")
    except:
        input("Error al crear el archivo CSV, presione enter para continuar...")

def editar_gasto():
    limpiar_pantalla()
    print("\tEDITAR GASTOS")
    if gastos:
        for i,gasto in enumerate(gastos):
            print(f"{i+1}) {gasto['categoria']} - ${gasto['monto']}")
        try:
            gasto = int(input("\nSeleccione un gasto: "))
            limpiar_pantalla()
            print(f"Gasto seleccionado: {gastos[gasto-1]['categoria']} - ${gastos[gasto-1]['monto']}")
            print("1) Categoría")
            print("2) Monto")
            opcion = input("\nSeleccione el gasto que desea editar: ")

            if opcion == "1":
                limpiar_pantalla()
                modificacion = input("Escriba la categoria: ").lower()
                gastos[gasto-1]["categoria"] = modificacion
                guardar_gastos()
                limpiar_pantalla()
                input("Gasto guardado correctamente, presione enter para continuar...")
            elif opcion == "2":
                limpiar_pantalla()
                try:
                    modificacion = float(input("Escriba el monto: "))
                    gastos[gasto-1]["monto"] = modificacion
                    guardar_gastos()
                    limpiar_pantalla()
                    input("Gasto guardado correctamente, presione enter para continuar...")
                except ValueError:
                    limpiar_pantalla()
                    input("INTRODUZCA UNICAMENTE VALORES NUMERICOS, PRESIONE ENTER PARA CONTINUAR...")
            else:
                limpiar_pantalla()
                input("OPCION NO VALIDA PRESIONE ENTER PARA CONTNIUAR...")

        except ValueError:
            limpiar_pantalla()
            input("INTRODUCE UNICAMENTE VALORES NUMERICOS, PULSE ENTER PARA CONTINUAR...")
        except IndexError:
            limpiar_pantalla()
            input("EL GASTO ES INVALIDO PRESIONE ENTER PARA CONTINUAR...")

cargar_gastos()
while True:
    limpiar_pantalla()
    print(""" SAVEWALLET
1) Agregar gastos
2) Gastos
3) Total
4) Filtrar por categoria
5) Borrar gasto
6) Editar Gasto
7) Exportar a CSV
X) Salir\n""")
    
    opcion = input("Seleccione la opción: ")

    if opcion == "1":
        agregar_gasto()
    elif opcion == "2":
        mostrar_gastos()
    elif opcion == "3":
        mostrar_total()
    elif opcion == "4":
        filtrar()
    elif opcion == "5":
        borrar_gastos()
    elif opcion == "6":
        editar_gasto()
    elif opcion == "7":
        exportar_csv()
    elif opcion.lower() == "x":
        break
    else:
        limpiar_pantalla()
        input("Opcion no válida presione enter para regresar al menú")
