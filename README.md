# Examen_tecnico
# Descripción del Ejercicio Técnico

Este ejercicio se desarrolló para resolver el problema de determinar si un número objetivo (`requiredSum`) puede formarse utilizando la suma de dos elementos diferentes de un array (`nums`).

## Lenguaje Utilizado

- **Lenguaje:** Python
- **Versión:** Python 3.10.5

## Herramientas y Entorno

- **Editor de Código:** Visual Studio Code 1.81.1
- **Formato del Código:** `black` 23.1.0 para la correcta estructuración del código.
- **Sistema Operativo:** Windows 10
- **Entorno de Desarrollo:** PowerShell 5.1

## Algoritmo Desarrollado

El algoritmo se basa en la utilización de un conjunto (`set`) para almacenar los elementos vistos mientras se itera sobre el array `nums`. El objetivo es verificar si el complemento de cada elemento actual ya ha sido visto antes. Si se encuentra dicho complemento, significa que se pueden sumar dos elementos para formar `requiredSum`, y se devuelve `True`. De lo contrario, el algoritmo devuelve `False`.

Este enfoque tiene una complejidad temporal de O(n) y espacial de O(n), siendo óptimo para la mayoría de los casos.

## Instrucciones para la Ejecución

1. Asegúrese de tener Python 3.10 o superior instalado en su sistema.
2. Coloque el archivo `app.py` en la misma carpeta que este `readme.txt`.
3. Desde la terminal, navegue a la carpeta donde se encuentra el archivo `app.py` y ejecute el siguiente comando:

   ```bash
   python app.py
