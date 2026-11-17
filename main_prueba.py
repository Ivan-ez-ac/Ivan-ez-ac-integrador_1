from funciones import *

# Datos hardcodeados SOLO PARA PRUEBAS (Nota 0 del TP).
# Los datos ya vienen cargados, por eso se pasa datos_cargados=True.
legajos = [20415, 20301, 20387, 20122, 20560, 20244]
apellidos_nombres = ["Perez Ana", "Gomez Luis", "Diaz Sol",
                    "Ruiz Marta", "Lopez Juan", "Mena Lucia"]
generos = ["F", "M", "X", "F", "M", "F"]
matriz = [
    [8, 9, 7, 10, 6],
    [6, 7, 5, 8, 9],
    [10, 10, 10, 10, 10],
    [5, 4, 6, 7, 3],
    [10, 8, 9, 10, 9],
    [7, 7, 8, 9, 6]
]

menu(
    legajos,
    apellidos_nombres,
    generos,
    matriz,
    True
)
