menu = {
    "A":{
        "Desayuno":{
            "a": {"Jugo especial": 15.00},
            "b": {"Jugo de fresa": 12.00},
            "c": {"Jugo de piña": 12.00},
            "d": {"Pan con chicharron": 10.00},
            "e": {"Pan con tamal": 18.00},
            "f": {"Club sandwich": 15.00},
            "g": {"Keke": 3.00}
            }
    },
    "B":{
        "Almuerzo":{
            "a": {"Lomo saltado": 20.00},
            "b": {"Tallarines verdes": 18.00},
            "c": {"Bistec": 20.00},
            "d": {"Cordon bleu": 18.00},
            "e": {"Chuleta": 20.00},
            "f": {"Aeropuerto especial": 20.00},
            "g": {"Papa rellena": 15.00}
                }
    },
    "C":{
        "Cena":{
            "a": {"Caldo de gallina": 10.00},
            "b": {"Aeropuerto": 12.00},
            "c": {"Jugo especial": 15.00},
            "d": {"Club sandwich": 15.00},
            "e": {"keke": 3.00}
            }
    },
    "D": {
        "Salir": None
    }
}

def imprimir_menu():
    print("------ Menú ------")
    print("A - Desayuno")
    print("B - Almuerzo")
    print("C - Cena")
    print("D - Salir")
    print("------------------")

def imprimir_submenu(submenu):
    print("------", list(submenu.keys())[0], "------")
    for key, value in list(submenu.values())[0].items():
        print(key + ")", list(value.keys())[0], "-", list(value.values())[0])
    print("-------------------")

opcion = ""
pedido = {}
while opcion != "D":
    imprimir_menu()
    opcion = input("Seleccione una opción: ")
    if opcion in ["A", "B", "C"]:
        submenu = menu[opcion]
        imprimir_submenu(submenu)
        opcion_producto = input("Seleccione un producto (ingrese letra y enter): ")
        if opcion_producto in submenu[list(submenu.keys())[0]]:
            producto = list(submenu[list(submenu.keys())[0]][opcion_producto].keys())[0]
            precio = list(submenu[list(submenu.keys())[0]][opcion_producto].values())[0]
            if producto in pedido:
                pedido[producto] += precio
            else:
                pedido[producto] = precio
            print("Usted ha agregado", producto, "por", precio, "soles")
        else:
            print("Opción no válida")
    elif opcion == "D":
        print("¡Hasta luego!\n")
    else:
        print("Opción no válida")

if len(pedido) > 0:
    print("\n------ Boleta ------")
    subtotal = 0
    for producto, precio in pedido.items():
        print(producto, "-", precio, "soles")
        subtotal += precio

    igv = subtotal * 0.18
    total = subtotal + igv

    print("--------------------")
    print("Subtotal: ", subtotal, "soles")
    print("IGV (18%): ", igv, "soles")
    print("Total: ", total, "soles\n")
