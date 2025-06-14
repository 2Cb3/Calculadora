# Funciones para las operaciones
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

# Diccionario para utitilizar las funciones segun lo que el usuario ingrese
opciones = {
    1: suma,
    2: resta,
    3: multiplicacion,
    4: division
}

# Diccionario que señala la operacion que ingreso el usuario sin repetir logica
nombres = {
    1: 'sumar',
    2: 'restar',
    3: 'multiplicar',
    4: 'dividir'
}

while True: # Imprimir el menu hasta que el usuario decida terminar el programa
    print("     ¡ Bienvenido a la Calculadora Basica !")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    
    try:     # " try " Para verificar si el usuario no ingreso un dato erroneo
        opcion = int(input("¿Que operacion desea realizar?: ")) # Toma un numero entero para buscarlo en el diccionario de opciones y asi no repetir logica
    except ValueError:
        print("Ops, parece que ingresaste un tipo de dato incorrecto.")
        exit()
    
    # Revisa que la opcion ingresada por el usuario este en el diccionario " opciones " y asi realizar la operacion que el usuario desea
    match opcion:
        case 1 | 2 | 3 | 4:
            print("     ¡ Buena eleccion !")
            try:
                # Pide al usuario ingresar los valores para las variables y asi poder realizar la operacion
                a = float(input(f"¿Cual es el primer valor a {nombres[opcion]}?: "))
                b = float(input("¿Cual es el segundo valor?: "))
            except ValueError:
                print("Ops, parece que ingresaste un dato incorrecto.")
                exit()
            resultado = opciones[opcion](a, b) # Busca la opcion que ingreso el usuario en el Diccionario que contiene las funciones, para despues realizar la operacion con las variables " a " y " b "
            print("     ¡ Gracias por usar el programa !")
            print(f"El resultado de {nombres[opcion]} {a} y {b} es de: {resultado}") # Da una respuesta personalizada, dependiendo de la operacion que el usuario escoja, sera la que se mostrara del diccionario " nombres "
        
        case 5: # Si el usuario ingreso el numero " 5 " el cual marca la opcion " Salir " en el menu
            print("Gracias por usar el programa.") # Imprime el mensaje de despedida para cerrar el bucle del programa
            break # Termina el programa
        
        case _: # Si el usuario ingreso un numero fuera del rango 1 - 5 imprime el mensaje de error
            print("Ops, parece que esa opcion no esta disponible.") # Mensaje de error