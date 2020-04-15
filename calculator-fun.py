def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def division_exacta(num1, num2):
    return num1 // num2

def elevar_cuadrado(num1):
    return num1 ** 2

def printRes(nombre, valor):
    print(f'El resultado de la {nombre} es: {valor}')

def get_num(num):
    return float(input(f'Dame el numero {num}: '))

def calculator():
    num1 = float(input('inserta el primer numero'))
    num2 = float(input('inserta el segundo numero'))

    printRes('Suma ', suma(num1,num2))
    printRes('Resta ', resta(num1,num2))
    printRes('Multiplicacion ', multiplicacion(num1,num2))
    printRes('Division ', division(num1,num2))
    printRes('Division exacta ', division_exacta(num1,num2))
    printRes('Elevar al cuadrado ', elevar_cuadrado(num1))
    printRes('Elevar al cuadrado ',elevar_cuadrado(num2))

calculator()
