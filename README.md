
# Estimador de Población de Plantas

Esta es una aplicación sencilla desarrollada en Python con la librería Tkinter, diseñada para ayudar a agricultores y técnicos a **estimar la población de plantas** por hectárea y por longitud de hilera, basándose en los espaciamientos de siembra.

## ¿Qué hace?

La aplicación permite al usuario ingresar el espaciamiento promedio entre hileras y el espaciamiento promedio entre plantas dentro de la hilera. También se puede ingresar opcionalmente una longitud específica de hilera. La aplicación calcula y muestra:

* La población estimada de plantas por hectárea.

* La población estimada de plantas por metro lineal de hilera.

* La población estimada de plantas para la longitud de hilera especificada (si se ingresó).

## Características

* Interfaz gráfica simple e intuitiva.

* Permite ingresar espaciamientos en metros o centímetros.

* Cálculo rápido de la población de plantas.

* Pestaña de información con la fórmula utilizada y notas importantes.

## Propósito

El objetivo de esta herramienta es facilitar el cálculo rápido de la densidad de siembra, lo cual es fundamental para la planificación, el seguimiento del cultivo y la estimación de rendimiento potencial en Agricultura de Precisión.

## Cómo usar

1. Ejecuta la aplicación (`estimador_poblacion.py` o el archivo ejecutable `.exe`).

2. Ve a la pestaña "Calculadora".

3. Ingresa el espaciamiento entre hileras.

4. Ingresa el espaciamiento entre plantas.

5. (Opcional) Ingresa una longitud de hilera específica.

6. Selecciona las unidades (metros o centímetros).

7. Haz clic en "Calcular Población".

8. Consulta la pestaña "Información" para entender los cálculos.

*Nota: Este es un cálculo teórico. La población real puede variar debido a la germinación, fallas en la siembra, etc.*

## Requisitos

* Python 3.x

* Librería Tkinter (generalmente incluida con la instalación estándar de Python)

## Instalación (desde código fuente)

1. Clona o descarga este repositorio.

2. Abre una terminal en la carpeta del proyecto.

3. Ejecuta el script: `python estimador_poblacion.py`

## Generar Ejecutable (.exe para Windows)

Puedes usar PyInstaller para crear un archivo ejecutable:

```bash
pip install pyinstaller
pyinstaller --onefile estimador_poblacion.py

Desarrollado por
LuisFarming

¡Espero que esta herramienta te sea de gran utilidad en tus labores agrícolas!
