import random

muro = "#"
espacio = " "
agente = "*"
espacioRecorrido = "·"
pelota = 'o'

def crear_mapa_laberinto(numero_filas, numero_columnas):
# Se crea un mapa lleno de paredes
    mapa_laberinto = []
    numero_paredes_generadas = 0
    for fila in range(0, numero_filas):
        fila_mapa_laberinto = []
        for columna in range(0, numero_columnas):
#             if (random.randrange(2) == 1 and numero_paredes_generadas < numero_paredes):
#                 fila_mapa_laberinto.append('#')
#                 numero_paredes_generadas += 1
#             else:
#                 fila_mapa_laberinto.append(' ')
            fila_mapa_laberinto.append(muro)
        mapa_laberinto.append(fila_mapa_laberinto)
        
#Se ubica aleatoriamente un punto de inicio y a partir de ese punto se llenan espacios
    numero_espacios_generados = 0
    fila_posicion_actual = random.randrange(numero_filas)
    columna_posicion_actual = random.randrange(numero_columnas)
    mapa_laberinto[fila_posicion_actual][columna_posicion_actual] = espacio
    numero_espacios_generados += 1

#Se ubica una ficha de manera aleatoria
    ficha_fila = random.randrange(numero_filas)
    ficha_columnas = random.randrange(numero_columnas)
    #mapa_laberinto[fila_posicion_actual][columna_posicion_actual] = agente

    while numero_espacios_generados < numero_espacios:
        direccion = random.randrange(4)
        if direccion == 0 and fila_posicion_actual > 0:
            fila_posicion_actual -= 1
        elif direccion == 1 and fila_posicion_actual < numero_filas - 1:
            fila_posicion_actual += 1
        elif direccion == 2 and columna_posicion_actual > 0:
            columna_posicion_actual -= 1
        else:
            if columna_posicion_actual < numero_columnas - 1:
                columna_posicion_actual += 1
            
        if mapa_laberinto[fila_posicion_actual][columna_posicion_actual] == muro:
            mapa_laberinto[fila_posicion_actual][columna_posicion_actual] = espacio
            numero_espacios_generados += 1
            
    return mapa_laberinto



def imprimir(l_i):
    for line in l_i:
        print(" ".join(map(str, line)))



def Agente(lab_ag, ff, cc, np):
    n = 1
    i = random.randrange(numero_filas)
    j = random.randrange(numero_columnas)
    while lab_ag[i][j] != espacio:
        i = random.randrange(numero_filas)
        j = random.randrange(numero_columnas)
    lab_ag[i][j] = agente
    n_E = (ff * cc) - np
    i_anterior = i
    j_anterior = j
    print("\n Intento " + str(n))
    imprimir(lab_ag)
    n_p = 0
    while n < n_E:# or n_p < n_P:
        direccion = random.randrange(4)
        if direccion == 0 and i > 0:
            #i_anterior = i
            i -= 1
        elif direccion == 1 and i < ff - 1:
            #i_anterior = i
            i += 1
        elif direccion == 2 and j > 0:
            #j_anterior = j
            j -= 1
        else:
            if j < cc - 1:
                #j_anterior = j
                j += 1
        if (
            lab_ag[i][j] != espacioRecorrido
            and lab_ag[i][j] != muro
            and lab_ag[i][j] != agente
        ):
            lab_ag[i_anterior][j_anterior] = espacioRecorrido
            i_anterior = i
            j_anterior = j
            lab_ag[i][j] = agente
            n += 1
            print("\n Intento " + str(n))
            imprimir(lab_ag)
        #if lab_ag[i][j] == pelota:
        #    np += 1
        '''elif lab_ag[i][j] == muro:
            i = i_anterior
            j = j_anterior'''

numero_filas = int(input('Introduzca el número de filas del laberinto: '))
numero_columnas = int(input('Introduzca el número de columnas del laberinto: '))
numero_paredes = int(input('Introduzca el número de paredes del laberinto: '))
numero_espacios = (numero_filas * numero_columnas) - numero_paredes

##laberinto = crear_mapa_laberinto(numero_filas, numero_columnas, numero_paredes, numero_espacios)

"""for fila_mapa_laberinto in laberinto:
    print(fila_mapa_laberinto)"""

laberinto_m = crear_mapa_laberinto(numero_columnas, numero_filas)
imprimir(laberinto_m)
Agente(laberinto_m, numero_filas, numero_columnas, numero_paredes)
#contador = contar_m(laberinto_m)