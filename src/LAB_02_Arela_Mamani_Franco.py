"""Laboratorio 02 · Visualización de campo vectorial — código plano (exportado del cuaderno).
Ejecutar bloque por bloque: cada bloque reutiliza las variables de los anteriores."""

# ===== Entorno =====
import sys, platform
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

plt.rcParams["figure.dpi"] = 110          # nitidez de las figuras exportadas
print("Python    :", platform.python_version())
print("NumPy     :", np.__version__)
print("Matplotlib:", matplotlib.__version__)
plt.show = lambda *a, **k: None  # ejecución sin ventanas


# ===== Bloque 1. Crear la grilla y los vectores =====
import numpy as np
import matplotlib.pyplot as plt

# La grilla contiene 17 x 17 posiciones
x = np.linspace(-4, 4, 17)
y = np.linspace(-4, 4, 17)
X, Y = np.meshgrid(x, y)

# En cada posición asignamos dos componentes del vector
U = -Y                   # Componente horizontal
V = X                    # Componente vertical

print("Puntos de la grilla:", X.size)
print("Vector en (X=2, Y=0):", U[8, 12], V[8, 12])
print("Vector en el centro:", U[8, 8], V[8, 8])


# ===== Bloque 2. Calcular la magnitud =====
# Calculamos una magnitud por cada vector
M = np.sqrt(U**2 + V**2)

print("Forma del campo U:", U.shape)
print("Magnitud en (2, 0):", round(M[8, 12], 2))
print("Magnitud en el centro:", round(M[8, 8], 2))
print("Magnitud máxima:", round(M.max(), 2))


# ===== Bloque 3. Dibujar flechas con quiver =====
plt.figure(figsize=(7, 6))
flechas = plt.quiver(X, Y, U, V, M, cmap="viridis")
plt.colorbar(flechas, label="Magnitud del vector")
plt.title("Campo vectorial: flechas de rotación")
plt.xlabel("Posición X")
plt.ylabel("Posición Y")
plt.axis("equal")
plt.show()


# ===== Bloque 4. Mostrar líneas de corriente =====
fig, ax = plt.subplots(figsize=(7, 6))
flujo = ax.streamplot(X, Y, U, V, color=M, cmap="viridis",
                      density=1.1)
fig.colorbar(flujo.lines, ax=ax, label="Magnitud")
ax.set_title("Campo vectorial: líneas de corriente")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_aspect("equal")
plt.show()


# ===== Bloque 5. Comparar una fuente y un sumidero =====
fig, axes = plt.subplots(1, 2, figsize=(11, 4))

# Fuente: las flechas salen del origen
axes[0].quiver(X, Y, X, Y, color="royalblue")
axes[0].set_title("Fuente: vectores hacia afuera")

# Sumidero: las flechas apuntan al origen
axes[1].quiver(X, Y, -X, -Y, color="darkorange")
axes[1].set_title("Sumidero: vectores hacia adentro")

for ax in axes:
    ax.set_aspect("equal")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
plt.tight_layout()
plt.show()


# ===== Reto 1. Grilla de 17 × 17 a 33 × 33 =====
# Misma fórmula con una grilla de 33 x 33 (1 089 vectores)
x33 = np.linspace(-4, 4, 33)
X33, Y33 = np.meshgrid(x33, x33)
U33, V33 = -Y33, X33
M33 = np.sqrt(U33**2 + V33**2)
print("Puntos:", X33.size, "| paso:", x33[1] - x33[0], "| magnitud máxima:", round(M33.max(), 2))

fig, axes = plt.subplots(1, 3, figsize=(15, 4.8))
casos = [("17 x 17 (289 flechas)", X, Y, U, V, M),
         ("33 x 33 (1 089 flechas)", X33, Y33, U33, V33, M33),
         ("33 x 33 submuestreada 1 de cada 2", X33[::2, ::2], Y33[::2, ::2], U33[::2, ::2], V33[::2, ::2], M33[::2, ::2])]
for ax, (titulo, xx, yy, uu, vv, mm) in zip(axes, casos):
    ax.quiver(xx, yy, uu, vv, mm, cmap="viridis")
    ax.set_title(titulo, fontsize=10)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_aspect("equal")
plt.tight_layout()
plt.show()


# ===== Reto 2. Densidad de streamplot: 0,5 y 2,0 =====
fig, axes = plt.subplots(1, 3, figsize=(15, 4.8))
for ax, d in zip(axes, [0.5, 1.1, 2.0]):
    flujo = ax.streamplot(X, Y, U, V, color=M, cmap="viridis", density=d)
    ax.set_title(f"density = {d}")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_aspect("equal")
    n_lineas = len(flujo.arrows.get_paths())          # una flecha por trayectoria
    n_tramos = len(flujo.lines.get_segments())        # tramos rectos que componen las líneas
    print(f"density = {d}: {n_lineas} líneas de corriente, {n_tramos} tramos dibujados")
plt.tight_layout()
plt.show()


# ===== Reto 3. Campo de silla: U = X, V = −Y =====
Us, Vs = X, -Y                       # campo de silla
Ms = np.sqrt(Us**2 + Vs**2)

# Vectores en puntos representativos (columna = x, fila = y)
for (px, py) in [(3, 0), (0, 3), (-3, 0), (0, -3), (2, 2), (0, 0)]:
    i, j = int((py + 4) / 0.5), int((px + 4) / 0.5)
    print(f"En ({px:>2}, {py:>2}) el vector es ({Us[i, j] + 0.0:+.0f}, {Vs[i, j] + 0.0:+.0f})")   # + 0.0 evita el "-0"

# Divergencia y rotacional numéricos de los cuatro campos del laboratorio
campos = {"Rotación (-Y, X)": (-Y, X), "Fuente (X, Y)": (X, Y),
          "Sumidero (-X, -Y)": (-X, -Y), "Silla (X, -Y)": (X, -Y)}
print()
print(f"{'Campo':<20}{'Divergencia':>12}{'Rotacional':>12}")
for nombre, (u, v) in campos.items():
    dudx, dudy = np.gradient(u, x, axis=1), np.gradient(u, y, axis=0)
    dvdx, dvdy = np.gradient(v, x, axis=1), np.gradient(v, y, axis=0)
    print(f"{nombre:<20}{(dudx + dvdy).mean():>12.1f}{(dvdx - dudy).mean():>12.1f}")

fig, axes = plt.subplots(1, 2, figsize=(11, 4.8))
axes[0].quiver(X, Y, Us, Vs, Ms, cmap="viridis")
axes[0].set_title("Silla: flechas (quiver)")
axes[1].streamplot(X, Y, Us, Vs, color=Ms, cmap="viridis", density=1.1)
axes[1].set_title("Silla: líneas de corriente")
for ax in axes:
    ax.set_aspect("equal")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
plt.tight_layout()
plt.show()
