from funciones import *

CANTIDAD_ESTUDIANTES = 30
CANTIDAD_MATERIAS = 5

legajos = [0] * CANTIDAD_ESTUDIANTES
apellidos_nombres = [""] * CANTIDAD_ESTUDIANTES
generos = [""] * CANTIDAD_ESTUDIANTES
matriz = crear_matriz(CANTIDAD_ESTUDIANTES, CANTIDAD_MATERIAS)

menu(
    legajos,
    apellidos_nombres,
    generos,
    matriz
)
