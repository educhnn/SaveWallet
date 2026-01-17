import os
from storage import guardar_gastos, cargar_gastos

gastos = cargar_gastos()

def pausa():
    input("Presione enter para continuar...")

def texto():
    return input("Seleccione la categoria: ").lower()

def enteros():
    return int(input("Introduzca una opción: "))

def floats():
    return float(input("Introduzca cuanto gastó: "))

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def agregar_gasto():
    limpiar_pantalla()
    try:
        monto = floats()
        categoria = texto()
        gasto = {
            "monto": monto,
            "categoria": categoria
        }
        gastos.append(gasto)
        guardar_gastos(gastos)
    except ValueError:
        limpiar_pantalla()
        print("Introduce un numero valido")
        pausa()
        return

def mostrar_gastos():
    limpiar_pantalla()
    print("\tGASTOS")
    for gasto in gastos:
        print(f"{gasto['categoria']} - ${gasto['monto']}")
    pausa()

def mostrar_total():
    total = 0
    limpiar_pantalla()
    print("\tTOTAL DE GASTOS")
    for gasto in gastos:
        total += gasto["monto"] 
    print(f"Usted gastó un total de: ${total}")
    pausa()

def filtrar():
    limpiar_pantalla()
    filtro = texto()
    limpiar_pantalla()
    print("\tFILTRO")
    encontrado = False

    for gasto in gastos:
        if gasto["categoria"] == filtro:
           print(f"{gasto['categoria']} - ${gasto['monto']}")
           encontrado = True
        
    if not encontrado:
        print("LA CATEGORIA NO EXISTE")
    pausa()

def borrar_gastos():
    limpiar_pantalla()
    print("\tBORRAR GASTOS")
    if gastos:
        for i, gasto in enumerate(gastos):
            print(f"{i+1}) {gasto['categoria']} - ${gasto['monto']}")
        try:
            opcion = enteros()
            gastos.pop(opcion-1)
            guardar_gastos(gastos)
        except IndexError:
            limpiar_pantalla()
            print("EL GASTO ES INVALIDO PRESIONE ENTER PARA CONTINUAR...")
            pausa()
        except ValueError:
            limpiar_pantalla()
            print("INTRODUCE UNICAMENTE VALORES NUMERICOS PRESIONA ENTER PARA CONTINUAR...")
            pausa()
    else:
        print("No existen gastos actualmente")
        pausa()

def exportar_csv():
    limpiar_pantalla()
    if not gastos:
        print("No existen gastos actualmente")
        pausa()
        return
    try:
        with open("gastos.csv", "w",encoding="utf-8")as archivo:
            archivo.write("categoria,monto\n")
            for gasto in gastos:
                archivo.write(f"{gasto['categoria']},{gasto['monto']}\n")
            print("Archivo creado correctamente...")
            pausa()
    except:
        print("Error al crear el archivo CSV")
        pausa()

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
            opcion = enteros()

            if opcion == 1:
                limpiar_pantalla()
                modificacion = texto()
                gastos[gasto-1]["categoria"] = modificacion
                guardar_gastos(gastos)
                limpiar_pantalla()
                print("Gasto guardado correctamente")
                pausa()
            elif opcion == 2:
                limpiar_pantalla()
                try:
                    modificacion = floats()
                    gastos[gasto-1]["monto"] = modificacion
                    guardar_gastos(gastos)
                    limpiar_pantalla()
                    print("Gasto guardado correctamente")
                    pausa()
                except ValueError:
                    limpiar_pantalla()
                    print("INTRODUZCA UNICAMENTE VALORES NUMERICOS")
                    pausa()
            else:
                limpiar_pantalla()
                print("OPCION NO VALIDA")
                pausa()

        except ValueError:
            limpiar_pantalla()
            print("INTRODUCE UNICAMENTE VALORES NUMERICOS")
            pausa()
        except IndexError:
            limpiar_pantalla()
            print("EL GASTO ES INVALIDO")
            pausa()

def main():
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
            print("Opcion no válida presione enter para regresar al menú")
            pausa()

if __name__ == '__main__':
    main()