import random

VOCALES = set('aeiou')

def letra_aleatoria():
    return chr(ord('a') + random.randint(0, 25))

def crear_palabra(n=4):
    if n == 0:
        return ''
    return letra_aleatoria() + crear_palabra(n - 1)

def crear_fila(tamaño, columnas_restantes=None):
    if columnas_restantes is None:
        columnas_restantes = tamaño
    if columnas_restantes == 0:
        return []
    return [crear_palabra(4)] + crear_fila(tamaño, columnas_restantes - 1)

def crear_matriz(tamaño, filas_restantes=None):
    if filas_restantes is None:
        filas_restantes = tamaño
    if filas_restantes == 0:
        return []
    return [crear_fila(tamaño)] + crear_matriz(tamaño, filas_restantes - 1)

def tiene_vocal(palabra, indice=0):
    if indice == len(palabra):
        return False
    if palabra[indice] in VOCALES:
        return True
    return tiene_vocal(palabra, indice + 1)

def contar_palabras_con_vocal_dc(matriz, f0, f1, c0, c1):
    if f0 >= f1 or c0 >= c1:
        return 0
    if f1 - f0 == 1 and c1 - c0 == 1:
        return 1 if tiene_vocal(matriz[f0][c0]) else 0
    fm = (f0 + f1) // 2
    cm = (c0 + c1) // 2
    return (
        contar_palabras_con_vocal_dc(matriz, f0, fm, c0, cm) +
        contar_palabras_con_vocal_dc(matriz, f0, fm, cm, c1) +
        contar_palabras_con_vocal_dc(matriz, fm, f1, c0, cm) +
        contar_palabras_con_vocal_dc(matriz, fm, f1, cm, c1)
    )

def _imprimir_fila(fila, indice=0, acumulado=''):
    if indice == len(fila):
        print(acumulado.rstrip())
        return
    nuevo_acumulado = acumulado + fila[indice] + (' ' if indice < len(fila) - 1 else '')
    _imprimir_fila(fila, indice + 1, nuevo_acumulado)

def imprimir_matriz(matriz, indice_fila=0):
    if indice_fila == len(matriz):
        return
    _imprimir_fila(matriz[indice_fila])
    imprimir_matriz(matriz, indice_fila + 1)

def principal():
    try:
        n = int(input('Ingrese el tamaño N de la matriz NxN: '))
    except Exception:
        n = 8
    if n <= 0:
        n = 8

    random.seed()
    m = crear_matriz(n)
    print('Matriz generada:')
    imprimir_matriz(m)
    total = contar_palabras_con_vocal_dc(m, 0, n, 0, n)
    print(f"\nTotal de palabras con al menos una vocal: {total} de {n*n}")

if __name__ == '__main__':
    principal()
