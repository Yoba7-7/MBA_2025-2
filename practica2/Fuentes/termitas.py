import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# --- PARÁMETROS DEL MODELO (entrada manual) ---
try:
    WIDTH = int(input("Ancho del mundo (ej. 50): "))
    HEIGHT = int(input("Alto del mundo (ej. 50): "))
    NUM_TERMITAS = int(input("Número de termitas (ej. 100): "))
    DENSIDAD = float(input("Porcentaje de densidad (0.0 a 1.0, ej. 0.1): "))
    MAX_TIEMPO = int(input("Cantidad de pasos (ej. 200): "))
except:
    print("Entrada inválida, usando valores por defecto.")
    WIDTH = 50
    HEIGHT = 50
    NUM_TERMITAS = 100
    DENSIDAD = 0.1
    MAX_TIEMPO = 200


# --- MUNDO Y SETUP ---

mundo = np.random.rand(WIDTH, HEIGHT) < DENSIDAD

# Cada termita tiene posición (x, y) y si está cargando una astilla
termitas = []
for _ in range(NUM_TERMITAS):
    termitas.append({
        "x": random.randint(0, WIDTH - 1),
        "y": random.randint(0, HEIGHT - 1),
        "cargando": False
    })

# Historial para guardar datos de gráficas
historial_activas = []
historial_cumulos = []

# ---MODELO---

# Mueve una termita a una posición vecina (arriba, abajo, izquierda, derecha)
def mover_termita(termita):
    dx, dy = random.choice([(1,0), (-1,0), (0,1), (0,-1)])
    termita["x"] = (termita["x"] + dx) % WIDTH
    termita["y"] = (termita["y"] + dy) % HEIGHT

# Ejecuta un paso del tiempo para todas las termitas
def paso_de_tiempo():
    for t in termitas:
        mover_termita(t)  # Se mueve
        x, y = t["x"], t["y"]

        # Si no está cargando y hay astilla, la recoge
        if not t["cargando"] and mundo[x, y]:
            t["cargando"] = True
            mundo[x, y] = False
        
        # Si está cargando y cae en otra astilla, suelta
        elif t["cargando"] and mundo[x, y]:
            t["cargando"] = False
        
        # Si está cargando y el patch está vacío, puede soltar con probabilidad
        elif t["cargando"] and not mundo[x, y] and random.random() < 0.05:
            mundo[x, y] = True
            t["cargando"] = False

# Cuenta cuántos cúmulos de astillas hay en el mundo
def contar_cumulos():
    visitado = np.zeros((WIDTH, HEIGHT), dtype=bool)
    num_cumulos = 0

    # DFS iterativo (sin recursión) para buscar cúmulos conectados
    def dfs(x, y):
        pila = [(x, y)]
        while pila:
            i, j = pila.pop()

            # Si está fuera del mundo o ya visitado o no hay astilla, ignorar
            if not (0 <= i < WIDTH and 0 <= j < HEIGHT):
                continue
            if visitado[i, j] or not mundo[i, j]:
                continue
            # Marcar como visitado y explorar vecinos
            visitado[i, j] = True
            vecinos = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
            pila.extend(vecinos)

    # Buscar todos los patches con astillas no visitados
    for i in range(WIDTH):
        for j in range(HEIGHT):
            if mundo[i, j] and not visitado[i, j]:
                dfs(i, j) # Explorar el cúmulo conectado
                num_cumulos += 1 # Cada DFS = un cúmulo

    return num_cumulos

# --- VISUALIZACIÓN ---
fig, ax = plt.subplots()
imagen = np.zeros((WIDTH, HEIGHT, 3), dtype=np.uint8)
im = ax.imshow(imagen, interpolation='nearest')

def actualizar(frame):
    paso_de_tiempo()

    # Dibujar mundo (astillas en color cafe)
    imagen[:, :, :] = 0
    imagen[mundo, :] = [168, 94, 50]  # Patches con astilla

    # Dibujar termitas
    for t in termitas:
        x, y = t["x"], t["y"]
        if t["cargando"]:
            imagen[x, y, :] = [255, 165, 0]  # Naranja
        else:
            imagen[x, y, :] = [255, 255, 255]  # Blanco

    activas = sum(1 for t in termitas if t["cargando"])
    cumulos = contar_cumulos()
    historial_activas.append(activas)
    historial_cumulos.append(cumulos)

    ax.set_title(f"Tiempo: {frame} | Activas: {activas} | Cúmulos: {cumulos}")
    im.set_data(imagen)
    return [im]

ani = animation.FuncAnimation(fig, actualizar, frames=MAX_TIEMPO, interval=100, repeat=False)
plt.show()


# Mostrar gráficas de actividad y cúmulos
plt.figure(figsize=(12, 5))

# Gráfica de termitas activas
plt.subplot(1, 2, 1)
plt.plot(historial_activas, color='orange')
plt.title("Termitas activas vs Tiempo")
plt.xlabel("Tiempo")
plt.ylabel("Número de termitas cargando")

# Gráfica de cúmulos de astillas
plt.subplot(1, 2, 2)
plt.plot(historial_cumulos, color='purple')
plt.title("Cúmulos de astillas vs Tiempo")
plt.xlabel("Tiempo")
plt.ylabel("Número de cúmulos")

plt.tight_layout()
plt.show()