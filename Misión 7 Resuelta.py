#Alberto Contreras Torres
# Resuelve divisiones entre distintos dividendos y divisores y saca el número más grande


def dividir(dividendo, divisor):
    cociente = 0
    residuo = dividendo
    while residuo >= divisor:
        residuo = residuo - divisor
        cociente = cociente + 1

    print(dividendo, "/", divisor, "=", cociente, ", sobra", residuo)



def encontrarMayor():
    print("Teclea una serie de números para encontrar el mayor")
    numero = int(input("Teclea un número [-1 para salir] :"))
    nMayor = -1
    while numero != -1 :

        if numero >= nMayor:
            nMayor = numero
            numero = int(input("Teclea un número [-1 para salir] :"))

        elif nMayor > numero:
            numero = int(input("Teclea un número [-1 para salir] :"))

    if nMayor != -1:
        print ("El número mayor es :", nMayor)

    else:
        print("No hay valor mayor")


def leerOpcionMenu():
    print("Misión 07. Ciclos while")
    print("Autor: Alberto Contreras Torres")
    print("Matricula: A01748151")
    print("1. Calcular divisiones")
    print("2. Encontrar el mayor")
    print("3. Salir")
    opcion = int(input("Teclea tu opción: "))
    return opcion


def main():
    opcion = leerOpcionMenu()
    while opcion != 3:
        if opcion == 1:
            dividendo = int(input("Tecela tu diviedendo :"))
            divisor = int(input("Teclea tu divisor :"))
            dividir(dividendo, divisor)
        elif opcion == 2:
            encontrarMayor()
        else:
            print("ERROR, teclea 1, 2 o 3")
        opcion = leerOpcionMenu()

    print("Gracias por usar este programa, regresa pronto")


main()

