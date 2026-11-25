# Laboratorio 02 · Visualización de campo vectorial

De componentes U y V a flechas y líneas de corriente

**Visualización de Datos** · Escuela Profesional de Ingeniería de Sistemas · Universidad Nacional del Altiplano – Puno
Estudiante: Franco · 25 de noviembre de 2026

Se visualizó un campo de rotación (U, V) = (−Y, X) sobre una grilla de 17 × 17 puntos con flechas (`quiver`) y líneas de corriente (`streamplot`), y se comparó una fuente con un sumidero. Tres retos exploraron la legibilidad de las flechas con más puntos, la densidad de las líneas de corriente y un campo de silla.

## Estructura

| Ruta | Contenido |
|---|---|
| `notebooks/LAB_02_Campo_Vectorial.ipynb` | Cuaderno ejecutado: bloques guiados, retos, respuestas y conclusiones |
| `src/LAB_02_Campo_Vectorial.py` | El mismo código en texto plano |
| `anexos/figuras/` | 6 figuras PNG extraídas del cuaderno |
| `anexos/salidas/` | Salidas de consola de cada bloque |
| `informe/` | Informe del laboratorio en `.docx` y `.pdf` |

## Cómo reproducirlo

```bash
pip install numpy matplotlib jupyter
jupyter notebook notebooks/LAB_02_Campo_Vectorial.ipynb
```

También puede abrirse en Google Colab (*Archivo → Abrir cuaderno → GitHub*, con la sesión de GitHub autorizada, ya que el repositorio es privado) y ejecutarse bloque por bloque con `Shift + Enter`.
Los datos son sintéticos: se generan en el propio código, por lo que no hay archivos de datos externos.
