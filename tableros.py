from typing import List, set, tuple

n: int = 10

Cantidad_Disparos: int = 15

Cantidad_Barcos: int = 5

Tablero: List[list[bool]] = []   

Disparos_realizados: set[tuple[int,int]] = set() #lo que chatGPT me explico acá es que puedo setear las columnas y las filas en las cual el usuario dispara con tuple[] y set(), para asi que no se pueda volver a disparar en el mismo lugar, pq sino se usaria list[]


aciertos: int = 0
fallos: int = 0



def crear_tablero_vacio(n: int) -> List[List[bool]]:
    """Crea un tablero de n x n lleno de False (sin barcos)."""
    return [[False for _ in range(n)] for _ in range(n)]


