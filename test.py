"""En este coódigo se desarrolla el famoso algoritmo el juego de la vida
creado por el matematico John Conway. Las reglas son simples
Para sectores poblados:
1.Una celula con 1 o 0 vecinos muere de soledad
2.Una celula con 4 o mas vecinos muero por sobrepoblación
3.Una celula con 2 o 3 vecinos vive
Para sectores no poblados:
1. Al haber 3 vecinos, una celula nace
"""
#importar librerias

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def tablero(Nx, Ny):
    # Creamos una matriz de tamaño Ny x Nx con valores aleatorios de 0 o 1 para el tablero
    Minterface= np.random.randint(2, size=(Ny, Nx))
    return Minterface

def actualizarReglas(Minterface):
    # Creamos una copia de la matriz para realizar operaciones
    NM = Minterface.copy()
    # Obtenemos el número de filas y columnas de la matriz original
    Ny, Nx = Minterface.shape
    # Iterar cada celula mediante fors para filas y columnas
    for i in range(Ny):
        for j in range(Nx):
            # Calculamos la suma de los valores de los vecinos en las posiciones i,j de la matriz
            total = (Minterface[i, (j-1)%Nx] + Minterface[i, (j+1)%Nx] +
                     Minterface[(i-1)%Ny, j] + Minterface[(i+1)%Ny, j] +
                     Minterface[(i-1)%Ny, (j-1)%Nx] + Minterface[(i-1)%Ny, (j+1)%Nx] +
                     Minterface[(i+1)%Ny, (j-1)%Nx] + Minterface[(i+1)%Ny, (j+1)%Nx])
            """La razón por la que se usa módulo (%) es para forzar la conversión de la matriz a una clase de toroide.
            Se aprovechan las caracteristicas de este para que los extremos de la matriz se unan y no se tengan que forzar condiciones de frontera.
            Esto hace que al llegar a un límite cualquiera de la matriz, el vecino proximo estará al inicio del extremo opuesto del límite 
            """
            # Aplicamos las reglas del juego
            #si en la posición (i,j) de la matriz hay una celula viva entonces...
            if Minterface[i, j] == 1:
                #si es menor a dos o mayor a tres la cantidad de vecinos la celula muere
                if total < 2 or total > 3:
                    NM[i, j] = 0
            else:
                #si a la celula la rodean 3 vecinos entonces la celula "vive"
                if total == 3:
                    NM[i, j] = 1
    return NM

def animate(i, img, Minterface):
    # Actualizamos la matriz para todas las filas y todas las columnas
    Minterface[:] = actualizarReglas(Minterface)
    # Actualizamos la imagen con los nuevos valores de la matriz
    img.set_array(Minterface)
    return img



# Parámetros de la simulación
Nx, Ny = 50, 50
Minterface = tablero(Nx, Ny)

# Configuración de la animación
fig, ax = plt.subplots()
img = ax.imshow(Minterface, interpolation='nearest')
ani = animation.FuncAnimation(fig, animate, fargs=(img, Minterface), frames=10, interval=200, save_count=50)

plt.show()
