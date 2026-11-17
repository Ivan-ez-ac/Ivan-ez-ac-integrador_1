"""
Biblioteca de funciones del TP Listas y Matrices.

Datos que se manejan (listas paralelas con las filas de la matriz):
    legajos (list): legajo de cada estudiante (entero de cinco cifras).
    apellidos_nombres (list): apellido y nombre de cada estudiante.
    generos (list): género de cada estudiante ("F", "M" o "X").
    matriz (list): matriz de calificaciones. Cada fila es un estudiante
                y cada columna es una materia.
    promedios (list): promedio de cada estudiante (se calcula en el ítem 3).
"""

LONGITUD_LEGAJO = 5
NOTA_MINIMA = 1
NOTA_MAXIMA = 10


# ---------------------------------------------------------------------------
# CREACIÓN DE LA MATRIZ
# ---------------------------------------------------------------------------
def crear_matriz(filas: int, columnas: int) -> list:
    """
    Crea una matriz de ceros con la cantidad de filas y columnas indicada.

    Argumentos:
        filas (int): cantidad de filas.
        columnas (int): cantidad de columnas.

    Retorno:
        list: matriz de ceros (cada fila es una lista distinta).
    """
    matriz = [0] * filas

    for i in range(filas):
        matriz[i] = [0] * columnas

    return matriz


def nombre_materia(indice: int) -> str:
    """
    Arma el nombre de una materia a partir del índice de su columna.
    La columna de índice 0 es MATERIA_1, la de índice 1 es MATERIA_2, etc.

    Argumentos:
        indice (int): índice de la columna de la matriz.

    Retorno:
        str: nombre de la materia (por ejemplo "MATERIA_1").
    """
    return f"MATERIA_{indice + 1}"


# ---------------------------------------------------------------------------
# VALIDACIONES
# ---------------------------------------------------------------------------
def es_numero(caracter: str) -> bool:
    """
    Indica si un carácter es un dígito del 0 al 9.

    Argumentos:
        caracter (str): carácter a evaluar.

    Retorno:
        bool: True si es un dígito, False en caso contrario.
    """
    retorno = False
    codigo = ord(caracter)

    if codigo >= 48 and codigo <= 57:
        retorno = True

    return retorno


def es_numerico(cadena: str) -> bool:
    """
    Indica si un texto no vacío está formado solo por dígitos.

    Argumentos:
        cadena (str): texto a evaluar.

    Retorno:
        bool: True si todos los caracteres son dígitos, False en caso
                contrario o si el texto está vacío.
    """
    retorno = cadena != ""

    for caracter in cadena:
        if es_numero(caracter) == False:
            retorno = False
            break

    return retorno


def es_letra(caracter: str) -> bool:
    """
    Indica si un carácter es una letra (mayúscula o minúscula, con o sin
    tilde, incluyendo la ñ y la ü).

    Argumentos:
        caracter (str): carácter a evaluar.

    Retorno:
        bool: True si es una letra, False en caso contrario.
    """
    retorno = False
    codigo = ord(caracter)

    if (codigo >= 65 and codigo <= 90) or \
        (codigo >= 97 and codigo <= 122) or \
        codigo == 193 or codigo == 201 or codigo == 205 or \
        codigo == 211 or codigo == 218 or codigo == 220 or \
        codigo == 225 or codigo == 233 or codigo == 237 or \
        codigo == 243 or codigo == 250 or codigo == 252 or \
        codigo == 209 or codigo == 241:
        retorno = True

    return retorno


def es_alfabetico(cadena: str) -> bool:
    """
    Indica si un texto está formado solo por letras y espacios, y tiene
    al menos una letra.

    Argumentos:
        cadena (str): texto a evaluar.

    Retorno:
        bool: True si es válido, False en caso contrario.
    """
    retorno = True
    hay_letra = False

    for caracter in cadena:
        if es_letra(caracter):
            hay_letra = True
        elif ord(caracter) != 32:
            retorno = False
            break

    if hay_letra == False:
        retorno = False

    return retorno


def es_genero(genero: str) -> bool:
    """
    Indica si un texto es un género válido: F, M o X (mayúscula o
    minúscula).

    Argumentos:
        genero (str): texto a evaluar.

    Retorno:
        bool: True si es válido, False en caso contrario.
    """
    retorno = False

    if genero == "F" or genero == "M" or genero == "X" or \
        genero == "f" or genero == "m" or genero == "x":
        retorno = True

    return retorno


def es_legajo(legajo: str) -> bool:
    """
    Indica si un texto es un legajo válido: un entero de cinco cifras
    (entre 10000 y 99999, sin cero a la izquierda).

    Argumentos:
        legajo (str): texto a evaluar.

    Retorno:
        bool: True si es válido, False en caso contrario.
    """
    retorno = False

    if es_numerico(legajo) and len(legajo) == LONGITUD_LEGAJO \
        and legajo[0] != "0":
        retorno = True

    return retorno


def es_nota(nota: str) -> bool:
    """
    Indica si un texto es una calificación válida: un entero entre 1 y 10.

    Argumentos:
        nota (str): texto a evaluar.

    Retorno:
        bool: True si es válida, False en caso contrario.
    """
    retorno = False

    if es_numerico(nota):
        valor = int(nota)
        if valor >= NOTA_MINIMA and valor <= NOTA_MAXIMA:
            retorno = True

    return retorno


def es_materia(materia: str, cantidad_materias: int) -> bool:
    """
    Indica si un texto es un número de materia válido: un entero entre
    1 y la cantidad de materias (índice de la columna más uno).

    Argumentos:
        materia (str): texto a evaluar.
        cantidad_materias (int): cantidad de materias (columnas).

    Retorno:
        bool: True si es válido, False en caso contrario.
    """
    retorno = False

    if es_numerico(materia):
        valor = int(materia)
        if valor >= 1 and valor <= cantidad_materias:
            retorno = True

    return retorno


# ---------------------------------------------------------------------------
# CARGA DE DATOS (ítem 1)
# ---------------------------------------------------------------------------
def cargar_legajo() -> int:
    """
    Pide un legajo por consola y lo valida hasta que sea un entero de
    cinco cifras.

    Retorno:
        int: legajo ingresado.
    """
    legajo = input("Ingrese el legajo (5 cifras): ")

    while es_legajo(legajo) == False:
        print("Error. El legajo debe ser un número entero de 5 cifras.")
        legajo = input("Ingrese el legajo (5 cifras): ")

    return int(legajo)


def cargar_apellido_nombre() -> str:
    """
    Pide el apellido y nombre por consola y lo valida hasta que
    contenga solo letras y espacios.

    Retorno:
        str: apellido y nombre ingresados.
    """
    nombre = input("Ingrese apellido y nombre: ")

    while es_alfabetico(nombre) == False:
        print("Error. Ingrese solamente letras y espacios.")
        nombre = input("Ingrese apellido y nombre: ")

    return nombre


def cargar_genero() -> str:
    """
    Pide el género por consola y lo valida hasta que sea F, M o X.
    Si se ingresa en minúscula, lo devuelve en mayúscula.

    Retorno:
        str: género ("F", "M" o "X").
    """
    genero = input("Ingrese el género (F/M/X): ")

    while es_genero(genero) == False:
        print("Error. Ingrese F, M o X.")
        genero = input("Ingrese el género (F/M/X): ")

    if genero == "f":
        genero = "F"
    elif genero == "m":
        genero = "M"
    elif genero == "x":
        genero = "X"

    return genero


def cargar_nota(indice_materia: int) -> int:
    """
    Pide la calificación de una materia por consola y la valida hasta
    que sea un entero entre 1 y 10.

    Argumentos:
        indice_materia (int): índice de la columna de la materia. Se usa
                    solo para armar el mensaje.

    Retorno:
        int: calificación ingresada.
    """
    mensaje = f"Ingrese la nota de {nombre_materia(indice_materia)} (1-10): "
    nota = input(mensaje)

    while es_nota(nota) == False:
        print("Error. Ingrese un entero entre 1 y 10.")
        nota = input(mensaje)

    return int(nota)


def cargar_estudiantes(legajos: list,
                        apellidos_nombres: list,
                        generos: list,
                        matriz: list) -> None:
    """
    Carga los datos de todos los estudiantes en las listas paralelas y
    en la matriz de calificaciones. La cantidad de estudiantes es el
    tamaño de las listas.

    Argumentos:
        legajos (list): lista de legajos.
        apellidos_nombres (list): lista de apellidos y nombres.
        generos (list): lista de géneros.
        matriz (list): matriz de calificaciones (estudiantes x materias).

    Retorno:
        None: modifica las listas y la matriz originales.
    """
    for i in range(len(legajos)):
        print(f"\nEstudiante {i + 1}")

        legajos[i] = cargar_legajo()
        apellidos_nombres[i] = cargar_apellido_nombre()
        generos[i] = cargar_genero()

        for j in range(len(matriz[i])):
            matriz[i][j] = cargar_nota(j)

    print("\nDatos cargados correctamente.")


# ---------------------------------------------------------------------------
# MOSTRAR ESTUDIANTES (ítems 2, 4 y 6)
# ---------------------------------------------------------------------------
def mostrar_estudiante(legajos: list,
                        apellidos_nombres: list,
                        generos: list,
                        matriz: list,
                        indice: int,
                        promedios: list = None) -> None:
    """
    Muestra en una fila los datos de UN estudiante (legajo, apellido y
    nombre, género, calificaciones y, si se recibe, su promedio).

    Argumentos:
        legajos (list): lista de legajos.
        apellidos_nombres (list): lista de apellidos y nombres.
        generos (list): lista de géneros.
        matriz (list): matriz de calificaciones.
        indice (int): posición del estudiante a mostrar.
        promedios (list): promedios de los estudiantes (opcional).

    Retorno:
        None.
    """
    fila = f"{legajos[indice]:<10}"
    fila += f"{apellidos_nombres[indice]:<28}"
    fila += f"{generos[indice]:<8}"

    for j in range(len(matriz[indice])):
        fila += f"{matriz[indice][j]:<11}"

    if promedios is not None and len(promedios) > indice:
        fila += f"{promedios[indice]:<10.2f}"

    print(fila)


def mostrar_estudiantes(legajos: list,
                        apellidos_nombres: list,
                        generos: list,
                        matriz: list,
                        promedios: list = None,
                        criterio: str = "TODOS",
                        valor: int = None) -> None:
    """
    Recorre todos los estudiantes y muestra, llamando a
    mostrar_estudiante, los que cumplan el criterio.

    Argumentos:
        legajos (list): lista de legajos.
        apellidos_nombres (list): lista de apellidos y nombres.
        generos (list): lista de géneros.
        matriz (list): matriz de calificaciones.
        promedios (list): promedios de los estudiantes (opcional).
        criterio (str): "TODOS" muestra a todos; "LEGAJO" muestra solo
                        al estudiante cuyo legajo es igual a valor.
        valor (int): legajo buscado cuando el criterio es "LEGAJO".

    Retorno:
        None.
    """
    if criterio == "LEGAJO":
        print("\n--- ESTUDIANTE ENCONTRADO ---")
    else:
        print("\n--- INFORME DE ESTUDIANTES ---")

    titulos = f"{'Legajo':<10}{'Apellido y nombre':<28}{'Género':<8}"

    for j in range(len(matriz[0])):
        titulos += f"{nombre_materia(j):<11}"

    if promedios is not None and len(promedios) > 0:
        titulos += f"{'Promedio':<10}"

    print(titulos)
    print("-" * len(titulos))

    for i in range(len(legajos)):
        if criterio == "TODOS" or \
            (criterio == "LEGAJO" and legajos[i] == valor):
            mostrar_estudiante(
                legajos,
                apellidos_nombres,
                generos,
                matriz,
                i,
                promedios
            )


# ---------------------------------------------------------------------------
# PROMEDIOS DE LOS ESTUDIANTES (ítem 3)
# ---------------------------------------------------------------------------
def calcular_promedio(notas: list) -> float:
    """
    Calcula el promedio de una lista de calificaciones (por ejemplo, una
    fila de la matriz), con dos decimales.

    Argumentos:
        notas (list): calificaciones de un estudiante.

    Retorno:
        float: promedio redondeado a 2 decimales.
    """
    suma = 0

    for i in range(len(notas)):
        suma += notas[i]

    return round(suma / len(notas), 2)


def calcular_promedios(matriz: list) -> list:
    """
    Calcula el promedio de cada estudiante (cada fila de la matriz) y
    lo guarda en una nueva lista.

    Argumentos:
        matriz (list): matriz de calificaciones.

    Retorno:
        list: lista de promedios, paralela a las demás listas.
    """
    promedios = [0.0] * len(matriz)

    for i in range(len(matriz)):
        promedios[i] = calcular_promedio(matriz[i])

    return promedios


def mostrar_promedios(apellidos_nombres: list, promedios: list) -> None:
    """
    Muestra una tabla con el apellido y nombre de cada estudiante y
    su promedio.

    Argumentos:
        apellidos_nombres (list): lista de apellidos y nombres.
        promedios (list): lista de promedios.

    Retorno:
        None.
    """
    titulos = f"{'Apellido y nombre':<28}{'Promedio':<10}"
    print(titulos)
    print("-" * len(titulos))

    for i in range(len(promedios)):
        print(f"{apellidos_nombres[i]:<28}{promedios[i]:<10.2f}")


# ---------------------------------------------------------------------------
# ORDENAMIENTO (ítem 4)
# ---------------------------------------------------------------------------
def intercambiar(lista: list, i: int, j: int) -> None:
    """
    Intercambia los elementos de las posiciones i y j de una lista.

    Argumentos:
        lista (list): lista a modificar (puede contener filas de una
                      matriz).
        i (int): primera posición.
        j (int): segunda posición.

    Retorno:
        None: modifica la lista original.
    """
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux


def ordenar_por_promedio(legajos: list,
                        apellidos_nombres: list,
                        generos: list,
                        matriz: list,
                        promedios: list,
                        orden: str) -> None:
    """
    Ordena a los estudiantes por promedio. Como las listas y la matriz
    son paralelas, cada intercambio se hace en todas ellas.

    Argumentos:
        legajos (list): lista de legajos.
        apellidos_nombres (list): lista de apellidos y nombres.
        generos (list): lista de géneros.
        matriz (list): matriz de calificaciones.
        promedios (list): lista de promedios.
        orden (str): "ASC" (menor a mayor) o "DESC" (mayor a menor).

    Retorno:
        None: modifica las listas y la matriz originales.
    """
    if orden != "ASC" and orden != "DESC":
        print('Error. El orden debe ser "ASC" o "DESC".')
    else:
        n = len(promedios)

        for i in range(n - 1):
            for j in range(i + 1, n):
                if (orden == "DESC" and promedios[j] > promedios[i]) or \
                    (orden == "ASC" and promedios[j] < promedios[i]):
                    intercambiar(legajos, i, j)
                    intercambiar(apellidos_nombres, i, j)
                    intercambiar(generos, i, j)
                    intercambiar(matriz, i, j)
                    intercambiar(promedios, i, j)


# ---------------------------------------------------------------------------
# MATERIAS CON MAYOR PROMEDIO GENERAL (ítem 5)
# ---------------------------------------------------------------------------
def calcular_promedio_materia(matriz: list, columna: int) -> float:
    """
    Calcula el promedio general de una materia (una columna de la
    matriz), con dos decimales.

    Argumentos:
        matriz (list): matriz de calificaciones.
        columna (int): índice de la columna (materia).

    Retorno:
        float: promedio de la materia redondeado a 2 decimales.
    """
    suma = 0

    for i in range(len(matriz)):
        suma += matriz[i][columna]

    return round(suma / len(matriz), 2)


def calcular_promedios_materias(matriz: list) -> list:
    """
    Calcula el promedio general de cada materia (cada columna de la
    matriz). La posición de la lista es el índice de la columna.

    Argumentos:
        matriz (list): matriz de calificaciones.

    Retorno:
        list: promedios de las materias.
    """
    promedios_materias = [0.0] * len(matriz[0])

    for j in range(len(matriz[0])):
        promedios_materias[j] = calcular_promedio_materia(matriz, j)

    return promedios_materias


def buscar_mayor(valores: list) -> float:
    """
    Busca el mayor valor de una lista.

    Argumentos:
        valores (list): lista de números (no vacía).

    Retorno:
        float: el mayor valor de la lista.
    """
    mayor = valores[0]

    for i in range(len(valores)):
        if valores[i] > mayor:
            mayor = valores[i]

    return mayor


def mostrar_materia(indice: int, promedio: float) -> None:
    """
    Muestra en una fila UNA materia con su promedio general.

    Argumentos:
        indice (int): índice de la columna de la materia.
        promedio (float): promedio general de la materia.

    Retorno:
        None.
    """
    print(f"{nombre_materia(indice):<14}{promedio:<10.2f}")


def mostrar_materias(promedios_materias: list,
                    criterio: str = "TODAS",
                    valor: float = None) -> None:
    """
    Recorre todas las materias y muestra, llamando a mostrar_materia,
    las que cumplan el criterio.

    Argumentos:
        promedios_materias (list): promedios generales de las materias.
        criterio (str): "TODAS" muestra todas; "MAYOR" muestra solo las
                        materias cuyo promedio es igual a valor.
        valor (float): promedio buscado cuando el criterio es "MAYOR".

    Retorno:
        None.
    """
    if criterio == "MAYOR":
        print("\n--- MATERIA/S CON MAYOR PROMEDIO GENERAL ---")
    else:
        print("\n--- PROMEDIO GENERAL DE LAS MATERIAS ---")

    titulos = f"{'Materia':<14}{'Promedio':<10}"
    print(titulos)
    print("-" * len(titulos))

    for i in range(len(promedios_materias)):
        if criterio == "TODAS" or \
            (criterio == "MAYOR" and promedios_materias[i] == valor):
            mostrar_materia(i, promedios_materias[i])


# ---------------------------------------------------------------------------
# BÚSQUEDA POR LEGAJO (ítem 6)
# ---------------------------------------------------------------------------
def buscar_indice_legajo(legajos: list, legajo_buscar: int) -> int:
    """
    Busca un legajo en la lista de legajos.

    Argumentos:
        legajos (list): lista de legajos.
        legajo_buscar (int): legajo a buscar.

    Retorno:
        int: posición donde está el legajo, o -1 si no existe.
    """
    indice = -1

    for i in range(len(legajos)):
        if legajos[i] == legajo_buscar:
            indice = i
            break

    return indice


def buscar_estudiante(legajos: list,
                    apellidos_nombres: list,
                    generos: list,
                    matriz: list,
                    legajo_buscar: int,
                    promedios: list = None) -> None:
    """
    Busca un estudiante por legajo y, si existe, muestra todos sus
    datos (incluyendo el promedio si ya fue calculado).

    Argumentos:
        legajos (list): lista de legajos.
        apellidos_nombres (list): lista de apellidos y nombres.
        generos (list): lista de géneros.
        matriz (list): matriz de calificaciones.
        legajo_buscar (int): legajo a buscar.
        promedios (list): promedios de los estudiantes (opcional).

    Retorno:
        None.
    """
    indice = buscar_indice_legajo(legajos, legajo_buscar)

    if indice == -1:
        print("No se encontró un estudiante con ese legajo.")
    else:
        mostrar_estudiantes(
            legajos,
            apellidos_nombres,
            generos,
            matriz,
            promedios,
            "LEGAJO",
            legajo_buscar
        )


# ---------------------------------------------------------------------------
# REPETICIÓN DE CALIFICACIONES EN UNA MATERIA (ítem 7)
# ---------------------------------------------------------------------------
def cargar_materia(cantidad_materias: int) -> int:
    """
    Pide por consola el número de una materia (índice de la columna más
    uno) y lo valida hasta que exista.

    Argumentos:
        cantidad_materias (int): cantidad de materias (columnas).

    Retorno:
        int: número de materia ingresado (entre 1 y cantidad_materias).
    """
    mensaje = f"Ingrese el número de materia (1-{cantidad_materias}): "
    materia = input(mensaje)

    while es_materia(materia, cantidad_materias) == False:
        print(f"Error. Ingrese un número entre 1 y {cantidad_materias}.")
        materia = input(mensaje)

    return int(materia)


def contar_calificaciones(matriz: list, materia: int) -> list:
    """
    Cuenta cuántas veces se repite cada calificación en una materia.

    Argumentos:
        matriz (list): matriz de calificaciones.
        materia (int): número de materia (índice de la columna más uno).

    Retorno:
        list: lista de 10 elementos. En el índice 0 está la cantidad de
              veces que se repite la nota 1, en el índice 1 la nota 2,
              y así hasta el índice 9, que corresponde a la nota 10.
    """
    cantidades = [0] * NOTA_MAXIMA
    columna = materia - 1

    for i in range(len(matriz)):
        nota = matriz[i][columna]
        cantidades[nota - 1] += 1

    return cantidades


def mostrar_repeticiones(cantidades: list, materia: int) -> None:
    """
    Muestra cuántas veces se repite cada calificación en una materia.

    Argumentos:
        cantidades (list): lista devuelta por contar_calificaciones.
        materia (int): número de materia (índice de la columna más uno).

    Retorno:
        None.
    """
    print(f"\n--- REPETICIÓN DE CALIFICACIONES EN {nombre_materia(materia - 1)} ---")

    for i in range(len(cantidades)):
        print(f"Nota {i + 1}: {cantidades[i]}")


# ---------------------------------------------------------------------------
# MENÚ
# ---------------------------------------------------------------------------
def mostrar_menu() -> None:
    """
    Muestra por consola las opciones del menú principal.
    """
    print("\n--- MENU DE ESTUDIANTES ---")
    print("1. Cargar datos")
    print("2. Mostrar todos los estudiantes")
    print("3. Calcular promedios")
    print("4. Mostrar estudiantes ordenados por promedio (DESC)")
    print("5. Mostrar materia/s con mayor promedio general")
    print("6. Buscar estudiante por legajo")
    print("7. Repetición de calificaciones en una materia")
    print("8. Salir")


def opcion_cargar_datos(legajos: list,
                        apellidos_nombres: list,
                        generos: list,
                        matriz: list) -> None:
    """
    Ítem 1 del menú: carga y valida los datos de todos los estudiantes.

    Argumentos:
        legajos (list): lista de legajos.
        apellidos_nombres (list): lista de apellidos y nombres.
        generos (list): lista de géneros.
        matriz (list): matriz de calificaciones.

    Retorno:
        None: modifica las listas y la matriz originales.
    """
    cargar_estudiantes(legajos, apellidos_nombres, generos, matriz)


def opcion_mostrar_estudiantes(legajos: list,
                            apellidos_nombres: list,
                            generos: list,
                            matriz: list) -> None:
    """
    Ítem 2 del menú: muestra el informe con todos los estudiantes.

    Argumentos:
        legajos (list): lista de legajos.
        apellidos_nombres (list): lista de apellidos y nombres.
        generos (list): lista de géneros.
        matriz (list): matriz de calificaciones.

    Retorno:
        None.
    """
    mostrar_estudiantes(legajos, apellidos_nombres, generos, matriz)


def opcion_calcular_promedios(apellidos_nombres: list, matriz: list) -> list:
    """
    Ítem 3 del menú: calcula el promedio de cada estudiante, lo guarda
    en una nueva lista y lo muestra.

    Argumentos:
        apellidos_nombres (list): lista de apellidos y nombres.
        matriz (list): matriz de calificaciones.

    Retorno:
        list: lista de promedios (paralela al resto de las listas).
    """
    promedios = calcular_promedios(matriz)

    print("\n--- PROMEDIOS DE LOS ESTUDIANTES ---")
    mostrar_promedios(apellidos_nombres, promedios)

    return promedios


def opcion_mostrar_ordenados(legajos: list,
                            apellidos_nombres: list,
                            generos: list,
                            matriz: list,
                            promedios: list) -> None:
    """
    Ítem 4 del menú: ordena a los estudiantes por promedio de manera
    descendente y muestra el informe.

    Argumentos:
        legajos (list): lista de legajos.
        apellidos_nombres (list): lista de apellidos y nombres.
        generos (list): lista de géneros.
        matriz (list): matriz de calificaciones.
        promedios (list): promedios de los estudiantes.

    Retorno:
        None: modifica las listas y la matriz originales (quedan
              ordenadas).
    """
    ordenar_por_promedio(
        legajos,
        apellidos_nombres,
        generos,
        matriz,
        promedios,
        "DESC"
    )

    mostrar_estudiantes(
        legajos,
        apellidos_nombres,
        generos,
        matriz,
        promedios
    )


def opcion_mayor_promedio_materia(matriz: list) -> None:
    """
    Ítem 5 del menú: calcula el promedio general de cada materia y
    muestra la/s materia/s con mayor promedio.

    Argumentos:
        matriz (list): matriz de calificaciones.

    Retorno:
        None.
    """
    promedios_materias = calcular_promedios_materias(matriz)
    mayor = buscar_mayor(promedios_materias)

    mostrar_materias(promedios_materias, "MAYOR", mayor)


def opcion_buscar_estudiante(legajos: list,
                            apellidos_nombres: list,
                            generos: list,
                            matriz: list,
                            promedios: list) -> None:
    """
    Ítem 6 del menú: pide un legajo y muestra los datos del estudiante
    junto con su promedio.

    Argumentos:
        legajos (list): lista de legajos.
        apellidos_nombres (list): lista de apellidos y nombres.
        generos (list): lista de géneros.
        matriz (list): matriz de calificaciones.
        promedios (list): promedios de los estudiantes.

    Retorno:
        None.
    """
    legajo_buscar = cargar_legajo()

    buscar_estudiante(
        legajos,
        apellidos_nombres,
        generos,
        matriz,
        legajo_buscar,
        promedios
    )


def opcion_contar_calificaciones(matriz: list) -> None:
    """
    Ítem 7 del menú: pide el número de una materia y muestra cuántas
    veces se repite cada calificación en ella.

    Argumentos:
        matriz (list): matriz de calificaciones.

    Retorno:
        None.
    """
    materia = cargar_materia(len(matriz[0]))
    cantidades = contar_calificaciones(matriz, materia)

    mostrar_repeticiones(cantidades, materia)


def opcion_salir() -> None:
    """
    Ítem 8 del menú: informa que el programa finaliza.
    """
    print("Saliendo del programa...")


def menu(legajos: list,
        apellidos_nombres: list,
        generos: list,
        matriz: list,
        datos_cargados: bool = False) -> None:
    """
    Controla el flujo del programa: muestra el menú, valida que se
    hayan cargado los datos (y calculado los promedios cuando
    corresponde) y llama a la función de cada ítem.

    Argumentos:
        legajos (list): lista de legajos.
        apellidos_nombres (list): lista de apellidos y nombres.
        generos (list): lista de géneros.
        matriz (list): matriz de calificaciones.
        datos_cargados (bool): True si las listas ya vienen con datos
                               (por ejemplo, datos hardcodeados para
                               pruebas). Por defecto es False.

    Retorno:
        None.
    """
    opcion = ""
    promedios_calculados = False
    promedios = []

    while opcion != "8":
        mostrar_menu()
        opcion = input("Ingrese una opcion: ")

        if opcion in ["2", "3", "4", "5", "6", "7"] and datos_cargados == False:
            print("Primero debe cargar los datos.")

        elif opcion in ["4", "6"] and promedios_calculados == False:
            print("Primero debe calcular los promedios.")

        else:
            match opcion:

                case "1":
                    opcion_cargar_datos(
                        legajos,
                        apellidos_nombres,
                        generos,
                        matriz
                    )
                    datos_cargados = True
                    # Los datos cambiaron: los promedios anteriores ya no sirven
                    promedios_calculados = False
                    promedios = []

                case "2":
                    opcion_mostrar_estudiantes(
                        legajos,
                        apellidos_nombres,
                        generos,
                        matriz
                    )

                case "3":
                    promedios = opcion_calcular_promedios(
                        apellidos_nombres,
                        matriz
                    )
                    promedios_calculados = True

                case "4":
                    opcion_mostrar_ordenados(
                        legajos,
                        apellidos_nombres,
                        generos,
                        matriz,
                        promedios
                    )

                case "5":
                    opcion_mayor_promedio_materia(matriz)

                case "6":
                    opcion_buscar_estudiante(
                        legajos,
                        apellidos_nombres,
                        generos,
                        matriz,
                        promedios
                    )

                case "7":
                    opcion_contar_calificaciones(matriz)

                case "8":
                    opcion_salir()

                case _:
                    print("Opcion invalida.")
