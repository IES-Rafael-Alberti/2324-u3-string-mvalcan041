
# "Práctica 3.0.4"
# Hay un método de cadenas llamado count que es similar a find, Escribe el código necesario para invocar a este método y contar el número de veces que una letra aparece en “banana”.

def contar_vocales(palabra: str, vocal: str) -> int:
    """Función que cuenta el número de veces que se repite una vocal en una palabra.

    Args:
        palabra (str): Palabra indicada por el usuario.
        vocal (str): Vocal, dada por el usuario, a buscar en la palabra.

    Returns:
        int: Devuelve el número de repeticiones de dicha vocal en la palabra en cuestión.
    """
    palabra = palabra.lower()
    vocal = vocal.lower()

    repeticiones_vocal = palabra.count(vocal)

    return repeticiones_vocal

def main():

    # Entrada:
    palabra = input("Indique una palabra:\n")
    vocal = input("Indique la vocal que desea buscar en la palabra:\n")

    # Procesamiento:
    repeticiones_vocal = contar_vocales(palabra, vocal)

    # Salida:
    print(f"El número de repeticiones de {vocal} en {palabra} es {repeticiones_vocal}.")


if __name__ == "__main__":
    main()
    