#colores
class bcolor:
    G = '\033[92m'
    R = '\033[91m'
    reset = '\033[0m'
#rut
def v_rut():
    while True:
        try:
            rut = int(input("ingrese su rut: "))
            if rut >= 1000000 and rut <=99999999:
                return rut
            else:
                print("rut invalido")
        except:
            print("debe ingresar un numero entero")
#nombre
def v_nom(p_texto: str, p_largo: int):
    while True:
        texto = input(f"ingrese su {p_texto}: ")
        if len(texto.strip()) >= p_largo and texto.isalpha():
            return texto
        else:
            print(f"Error!! El {p_texto} deve tener al menos {p_largo} leetras")
#correo
def v_correo():
    while True:
        correo = input("ingrese su correo: ")
        if "@" in correo.strip():
            return correo
        else:
            print("Correo mal ingresado")
#telefono
def v_cell():
    while True:
        try:
            cell = int(input("ingrese su numero de telefono: "))
            if len(str(cell)) == 9:
                return cell
            else:
                print("numero de celular incorrecto")
        except:
            print("numero de celular incorrecto")
#descuento
def v_descuento():
    while True:
        try:
            des = int(input("ingrese descuento a realizar: "))
            if des >= 0 and des <= 100:
                return des
            else:
                print("el descuento debe partir en 1 hasta 100")
        except:
            print("debe ingresar un n umero entero pocitivo")
#valor
def v_producto():
    while True:
            try:
                valor = int(input("ingrese el valor del producto: "))
                if valor >0:
                    break
                else:
                    print("valor ingresado incorrecto")
            except:
                print("debe ingresar un numero entero positivo")
#np.empty(_,_)
# validad cantidad
def v_cantidad():
    while True:
        try:
            cant = int(input("ingrese cantidad del producto: "))
            if cant >= 1:
                break
            else:
                print("Error! debe llevar desde 1 producto en adelante")
        except:
            print("Error! debe ingresar un numero entero positivo")