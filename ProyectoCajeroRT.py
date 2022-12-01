###########################################################################
# Simular cajero
###########################################################################

def cajero():
    print("Hola Bienvenido al cajero de codo a codo")
    idioma = int(input(
        "ingresa \n 1 para elegir el idioma en español \n 2 para ingles \n 3 para portugues: "))
    if idioma == 1:
        print("has seleccionado el idioma español")
        print("ingresa tu clave para acceder a tu cuenta \n la clave es 1234 ")
        clave = int(input("ingresa tu clave: "))
        nombre = str(input("ingresa tu nombre: "))
        saldo = float(85200)
        disponible = float(15000)
        saldoDolar = float(0)
        if clave == 1234:
            print("#########################################")
            print("Bienvenido a tu cuenta", nombre, "!!")
            print("#########################################")
            print("seleciona una opcion y presiona lo siguiente: ")
            print("#########################################")
            print("     #1  consultar saldo")
            print("     #2  depositar dinero")
            print("     #3  extraer dinero")
            print("     #4  transferir dinero")
            print("     #5  comprar dolares")
            print("     #6  vender dolares")
            print("     #7  crear plazo fijo")
            print("     #8  ver ultimos movimientos")
            print("     #9  salir de la cuenta")
            print("#########################################")
            opcion = int(input("ingresa tu opcion: "))
            # 1consultar saldo
            if opcion == 1:
                print("tu saldo actual en pesos es de: $", saldo)
            # 2depositar dinero
            elif opcion == 2:
                print("#########################################")
                ingreso = int(input(
                    "digite por teclado el monto de su dinero a ingresar y luego inserte su dinero: "))
                print("#########################################")
                saldoActual = saldo + ingreso
                print(
                    "--Gracias por ingresar su dinero, su saldo actual es de: $", saldoActual, "--")
            # 3extraer dinero
            elif opcion == 3:
                extraccion = int(input("ingresa el monto a extraer: "))
                saldoActual = saldo - extraccion
                print("gracias por extraer, tu saldo restante es: $", saldoActual)
            # 4transferir dinero
            elif opcion == 4:
                tranferir = int(
                    input("ingrese el cbu de la cuenta a la cual deseas tranferir: "))
                monto = int(input("ingresa el monto a tranferir: "))
                print("#########################################################")
                print("Estas por realizar una transferencia al numero de cuenta ", tranferir,
                      "con el siguiente monto: ", monto, "estas seguro que deseas realizar esta accion ?")
                print("#########################################################")
                saldoActual = saldo - monto
                confirmar = str(input(
                    "ingresa: \n     # si para confirmar la transferencia. \n     # no para cancelar: \n "))
                if confirmar == "si":
                    print(
                        "gracias tu tranferencia ha sido realizada!, tu saldo actual es de: $", saldoActual)
                elif confirmar == "no":
                    print("has cancelado tu transferencia")
                else:
                    print("has ingresado un valor invalido")
            # 5comprar dolares
            elif opcion == 5:
                print("#####################################")
                print("    el precio del dolar es de $160")
                print("    tu saldo es el siguiente: ", saldo)
                print("#####################################")
                compraDolar = float(
                    input("ingresa el monto de dolares a comprar: "))
                print("#####################################")
                print("estas seguro de comprar : u$s",
                      compraDolar, " dolares ?")
                confirma = str(
                    input("ingresa \n     #si para confirmar. \n     #no para cancelar "))
                print("#####################################")
                if confirma == "si":
                    conversion = compraDolar * 160
                    saldoActual = saldo - conversion
                    saldoDolar = saldoDolar + compraDolar
                    print("#####################################################")
                    print("tu saldo en tu cuenta pesos es de: $", saldoActual)
                    print("tu saldo en tu cuenta dolares es de: u$s", saldoDolar)
                    print("#####################################################")
                elif confirma == "no":
                    print("has cancelado tu compra")
            # 6vender dolares
            elif opcion == 6:
                print("#####################################")
                print("    el precio del dolar es de $160")
                print("    tu saldo es el siguiente: ", saldo)
                print("#####################################")
                venderDolar = float(
                    input("ingresa el monto de dolares a vender: "))
                print("#####################################")
                print("estas seguro de vender : u$s",
                      venderDolar, " dolares ?")
                confirma = str(
                    input("ingresa \n     #si para confirmar. \n     #no para cancelar "))
                print("#####################################")
                if confirma == "si":
                    conversion = venderDolar * 160
                    saldoActual = saldo + conversion
                    saldoDolar = saldoDolar - venderDolar
                    print("#####################################################")
                    print("tu saldo en tu cuenta pesos es de: $", saldoActual)
                    print("tu saldo en tu cuenta dolares es de: u$s", saldoDolar)
                    print("#####################################################")
                elif confirma == "no":
                    print("has cancelado tu venta")

            # 7crear plazo fijo
            elif opcion == 7:
                print("#####################################")
                print("    Tasa Nominal Anual (TNA) es de 75,00%")
                print("    la Tasa Efectiva Anual (TEA) es de 107,05%")
                print("    tu saldo es el siguiente: ", saldo)
                print("#####################################")
                plazoFijoMonto = float(
                    input("ingresa el capital a invertir: "))
                print("#####################################")
                plazoFijoDias = float(
                    input("ingresa el plazo en dias: "))
                print("#####################################")
                print("quiere que simulemos su plazo fijo en pesos por",
                      plazoFijoMonto, " pesos a ?", plazoFijoDias, " dias?")
                confirma = str(
                    input("ingresa \n     #si para confirmar. \n     #no para cancelar "))
                print("#####################################")
                if confirma == "si":
                    tasaInt = (75/100)
                    nDias = plazoFijoDias/365
                    simulador = plazoFijoMonto * (1+(tasaInt*nDias))
                    saldoActual = saldo - plazoFijoMonto
                    intGanados = (plazoFijoMonto - simulador) * -1
                    print("#####################################################")
                    print("tu saldo en tu cuenta pesos es de: $", saldoActual)
                    print("tu capital invertido es de: $", plazoFijoMonto)
                    print("tu interes ganado va a ser de : $", intGanados)
                    print("tu saldo en tu cuenta dolares es de: u$s", saldoDolar)
                    print("#####################################################")
                elif confirma == "no":
                    print("has cancelado tu venta")

            # 8ver ultimos movimientos
            elif opcion == 8:
                from os import system
                system("cls")
                listaMovimientos = ['Saldo actual: 85.200 Pesos ', 'Disponible para extraccion: 15.000 Pesos',
                                    'Saldo de dolares: 0,00', 'No tiene movimientos registrados']
                contenido = open("C:/Users/rrodriguez/Misdatos.txt", "w")
                for movimiento in listaMovimientos:
                    contenido.write(movimiento + "\n")
                contenido.close()
                print('Ahora lo abrimos!')
                contenido = open("C:/Users/rrodriguez/Misdatos.txt", "r")
                contador = 1
                for linea in contenido:
                    print("Linea", contador, ":", linea)
                    contador = contador + 1

            # 9salir de la cuenta
            elif opcion == 9:
                print("#####################################")
                print("    Has cancelado la transacción...")
                print("    Muchas gracias por usar nuestro cajero")
                print("    Que tenga un buen dia!!!")
                print("#####################################")

        else:
            print("clave incorrecta")
    elif idioma == 2:
        print("has seleccionado ingles")
    elif idioma == 3:
        print("has seleccionado portugues")
    else:
        print("opcion incorrecta")


cajero()
