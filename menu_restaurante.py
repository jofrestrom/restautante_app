from funciones import *
import numpy as np
import os
import time
import msvcrt
lista_aciento = []
lista_rut = []
lista_nombres = []
lista_correo = []
lista_fila = []
lista_columna = []
arreglo_rest = np.zeros((3,3), int)
iva = 0.19
acumulador_P = 0
cocacola = 1000
pepsi = 1300
cerveza = 1000
carbonada = 2000
bistec = 3000
hamburgesa = 1500
leche_asada = 2000
helado = 1000
pastel = 500
while True:
    os.system('cls')
    print("""
    1. ver
    2. reserva.
    3. carta
    4. pagar
    5. cancelar reserva
    6. salir""")
    while True:
        try:
            opc = int(input("ingrese opcion a ejecutar: "))
            if opc in(1,2,3,4,5,6):
                break
            else:
                print(bcolor.R + "opcion ingresado incorrecto" + bcolor.reset)
        except:
            print(bcolor.R + "debe ingresar un numero entero pocitivo" + bcolor.reset)
    os.system('cls')
    if opc == 1:
        print("cant personas")
        for x in range(3):#fila
            print(f"{(x+1)*2} personas | ", end=" ")
            for y in range(3):#columna
                if arreglo_rest[x][y] == 0:
                    print(bcolor.G + F"{arreglo_rest[x][y]}", end=" " + bcolor.reset)
                else:
                    print(bcolor.R + F"{arreglo_rest[x][y]}", end=" " + bcolor.reset)
            print()
        print("\t   ---------")
        print("\t      1 2 3")
        print("\t    columnas")
        print("precione cualquier tecla para continuar")
        msvcrt.getch()
    elif opc == 2:
        if 0 not in arreglo_rest:
            print("no quedan hacientos libre")
            continue
        print("RESERVA")
        rut = v_rut()
        if rut in lista_rut:
            print("este rut ya esta ingresado en el sistema")
            continue
        nom = v_nom("nombre", 3)
        correo = v_correo()
        lista_rut.append(rut)
        lista_nombres.append(nom)
        lista_correo.append(correo)
        while True:
            try:
                cant_personas = int(input("ingrese la cantidad de personas: "))
                if cant_personas >= 1 and cant_personas <= 6:
                    break
                else:
                    print("Error! debe ingresar por lo menos 1 persona")
            except:
                print("Error! debe ingresar un numero entero positivo")
        while True:
            if cant_personas >= 1 and cant_personas <= 2:
                largo_p = 3
            elif cant_personas >= 3 and cant_personas <=5:
                largo_p = 2
            elif cant_personas >= 5 and cant_personas <= 6:
                largo_p = 1
            print("cant personas")
            for x in range(largo_p):#fila
                if cant_personas >= 1 and cant_personas <= 2:
                    print(f"{(x+1)*2} personas | ", end=" ")
                elif cant_personas >= 3 and cant_personas <=4:
                    print(f"{(x+2)*2} personas | ", end=" ")
                elif cant_personas >= 5 and cant_personas <= 6:
                    print(f"{(x+3)*2} personas | ", end=" ")
                for y in range(3):#columna
                    if arreglo_rest[x][y] == 0:
                        print(bcolor.G + F"{arreglo_rest[x][y]}", end=" " + bcolor.reset)
                    else:
                        print(bcolor.R + F"{arreglo_rest[x][y]}", end=" " + bcolor.reset)
                print()
            print("\t   ---------")
            print("\t      1 2 3")
            print("\t    columnas")
            while True:
                    try:
                        fila = int(input("ingrese la fila a comprar: "))
                        if fila in(1,2,3):
                            break
                        else:
                            print("no exciste esta fila, las opciones son 1,2,3")
                    except:
                        print("debe ingresar un numero entero positivo")
            while True:
                try:
                    columna = int(input("ingrese la columna a comprar: "))
                    if columna in (1,2,3):
                        break
                    else:
                        print("columna incorrecta, las opciones son 1,2,3")
                except:
                    print("debe ingresar un numero entero")
            if arreglo_rest[fila-1][columna-1] == 0:
                arreglo_rest[fila-1][columna-1] = 1
                lista_fila.append(fila-1)
                lista_columna.append(columna-1)
                print("compra realizada con exito")
                break
            else:
                print("mesa ocupada")
            time.sleep(3)
    elif opc == 3:
        os.system('cls')
        rut = v_rut()
        if rut in lista_rut:
            while True:
                os.system('cls')
                print("""
        1. bebida
        2. platos
        3. postre
        4. pedir
        5. cancelar
        6. volver al menu principal""")
                while True:
                    try:
                        opc = int(input("ingrese opcion a pedir: "))
                        if opc in(1,2,3,4,5,6):
                            break
                        else:
                            print("opcion ingresada incorrecta")
                    except:
                        print("debe ingresar un numero entero pocitivo")
                if opc== 1:
                    while True:
                        os.system('cls')
                        print(f"""
        1. cocacola ${cocacola}
        2. cerveza ${cerveza}
        3. pepsi ${pepsi}
        4. volver al menu principal""")
                        while True:
                            try:
                                opc = int(input("ingrese numero de bebida a comprar: "))
                                if opc in(1,2,3,4):
                                    break
                                else:
                                    print("opcion de bebida incorrecta")
                            except:
                                print("debe ingresar un numero entero pocitivo")
                        if opc in (1,2,3):
                            while True:
                                try:
                                    cant = int(input("ingrese cantidad del producto: "))
                                    if cant >= 1:
                                        break
                                    else:
                                        print("Error! debe llevar desde 1 producto en adelante")
                                except:
                                    print("Error! debe ingresar un numero entero positivo")
                        if opc == 1:
                            CF = cant * cocacola
                            acumulador_P = CF
                        elif opc == 2:
                            CF = cant * cerveza
                            acumulador_P = CF
                        elif opc == 3:
                            CF = cant * pepsi
                            acumulador_P = CF
                        else:
                            print("volviendo al menu principal")
                            time.sleep(2)
                            break
                elif opc == 2:
                    os.system('cls')
                    print(f"""
        1. carbonada ${carbonada}
        2. bistec ${bistec}
        3. hamburgesa ${hamburgesa}
        4. volver al menu""")
                    while True:
                        try:
                            opc = int(input("ingrese el numero del plato deceado: "))
                            if opc in(1,2,3,4):
                                break
                            else:
                                print("opcion ingresada incorrrecta")
                        except:
                            print("Error! debe ingresar un numero entero pocitivo")
                    if opc in (1,2,3):
                            while True:
                                try:
                                    cant = int(input("ingrese cantidad del producto: "))
                                    if cant >= 1:
                                        break
                                    else:
                                        print("Error! debe llevar desde 1 producto en adelante")
                                except:
                                    print("Error! debe ingresar un numero entero positivo")
                    if opc == 1:
                        CF = cant * carbonada
                        acumulador_P = CF
                    elif opc == 2:
                        CF = cant * bistec
                        acumulador_P = CF
                    elif opc == 3:
                        CF = cant * hamburgesa
                        acumulador_P = CF
                    else:
                        print("volviendo al menu principal")
                        time.sleep(2)
                        break
                elif opc == 3:
                    while True:
                        os.system('cls')
                        print(f"""menu postre
        1. leche asada ${leche_asada}
        2. helado ${helado}
        3. pastel ${pastel}
        4. salir""")
                        while True:
                            try:
                                opc = int(input("ingrese opcion de postre elejida: "))
                                if opc in(1,2,3,4):
                                    break
                                else:
                                    print("opcion ingresado incorrecto")
                            except:
                                print("Error debe ingresar un numero entero pocitivo")
                        if opc in (1,2,3):
                            while True:
                                try:
                                    cant = int(input("ingrese cantidad del producto: "))
                                    if cant >= 1:
                                        break
                                    else:
                                        print("Error! debe llevar desde 1 producto en adelante")
                                except:
                                    print("Error! debe ingresar un numero entero positivo")
                        if opc == 1:
                            CF = cant * leche_asada
                            acumulador_P = CF
                        elif opc == 2:
                            CF = cant * helado
                            acumulador_P = CF
                        elif opc == 3:
                            CF = cant * pastel
                            acumulador_P = CF
                        else:
                            print("volviendo al menu principal")
                            time.sleep(2)
                            break
                elif opc == 4:
                    print(f"total a pagar: ${acumulador_P}")
                    while True:
                        selec = str(input("confirme monto: "))
                        if selec.upper() in("SI", "NO"):
                            break
                        else:
                            print("seleccion incorrecta, las respuesta son SI o NO")
                    if selec.upper() == "SI":
                        print("")
                        acumulador_P = acumulador_P
                        break
                    else:
                        continue
                elif opc == 5:
                    print(f"total a pagar: ${acumulador_P}")
                    while True:
                        selec = str(input("esta seguro que desea cancelar esta compra: "))
                        if selec.upper in("SI", "NO"):
                            break
                        else:
                            print("seleccion incorrecta, las respuesta son SI o NO")
                    if selec.upper() == "SI":
                        print("CANCELANDO COMPRA")
                        time.sleep(3)
                        acumulador_P = 0
                        break
                    else:
                        continue
                else:
                    print("volviendo al menu principal")
                    time.sleep(2)
                    break
    elif opc == 4:
        #des = v_descuento()
        #des2 = acumulador_P - des
        #valor_iva = acumulador_P * 0.19
        #valor_iva2 = acumulador_P - valor_iva
        #total = des2 + valor_iva2
        #print(f"""boleta
        #subtotal: {acumulador_P}
        #iva 19%: {iva}
        #descuento: {des}""")
        pass
    elif opc == 5:
        rut = v_rut()
        pos = lista_rut.index(rut)
        if rut in(lista_rut):
            while True:
                selec = str(input("esta seguro que desea cancelar esta reserva: "))
                if selec.upper in("SI", "NO"):
                    break
                else:
                    print("seleccion incorrecta, las respuesta son SI o NO")
            if selec.upper() == "SI":
                print("CANCELANDO RESERVA")
                time.sleep(3)
                acumulador_P = 0
                break
            lista_rut.pop(pos)
            lista_nombres.pop(pos)
            lista_correo.pop(pos)
            fila = lista_fila[pos]
            columna = lista_columna[pos]
            arreglo_rest[fila][columna] = 0
            lista_fila.pop(pos)
            lista_columna.pop(pos)
            print("reserva eliminada con exito")
            time.sleep()
    else:
        print("cerrando sistema...")
        time.sleep(2)
        break