
# "Práctica 3.0.3"

"""palabra = 'banana'
contador = 0
for letra in palabra:
    if letra == 'a':
        contador = contador + 1
print(contador)"""

# Encapsúlalo en una función llamada cuenta, y hazla genérica de tal modo que pueda aceptar una cadena y una letra como argumentos.

def cuenta(palabra: str) -> int:
    """Función que espera un str, analiza cuántas letras 'a' hay en la palabra y devuelve un número entero.

    Args:
        palabra (str): Palabra indicada por el usuario, de tipo str.

    Returns:
        int: Devuelve las repeticiones de la letra concretada, de tipo int.
    """
    contador = 0
    
    for letra in palabra:
        if letra  == "a":
            contador = contador + 1
    
    return contador

def main():
    
    # Entrada:
    palabra = input(f"Indique una palabra:\n")

    # Procesamiento:
    num_letra_repetida = cuenta(palabra)

    # Salida:
    print(f"El número de 'a' es: {num_letra_repetida}")


if __name__ == "__main__":
    main()