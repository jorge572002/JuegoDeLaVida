#importación de librerias
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from GOLFunctions import tablero, actualizarReglas

def animate(i, img, Minterface):
    Minterface[:] = actualizarReglas(Minterface)
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
