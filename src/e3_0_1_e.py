
# "Práctica 3.0.1"
# Escribe un bucle while que comience con el último carácter en la cadena y haga un recorrido hacia atrás hasta el primer carácter en la cadena, imprimiendo cada letra en una línea independiente.

def cadena (palabra:str) -> str:
    """Función que devuelve en varias líneas los caracteres de la palabra que se le ha indicado, de tipo str.

    Args:
        palabra (str): Input de tipo str que indica el usuario.

    Returns:
        str: Varias líneas con los caracteres de la palabra indicada por el usuario.
    """
    longitud = len(palabra)
    letra_indice = longitud - 1

    while letra_indice >= 0:
        print (palabra[letra_indice])
        letra_indice -= 1

def main():
    
    # Entrada:
    palabra = input(f"Indique una palabra:\n")

    # Procesamiento:
    cad_palabra = cadena(palabra)

    # Salida:
    print(cad_palabra)
    
if __name__ == "__main__":
    main()

# Ver bien, devuelve "none", error.