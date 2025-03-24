#   Codigo que implementa el metodo de la regla de Simpson 
#   para aproximar la integral
#   
#
#           Autor:
#   Dr. Ivan de Jesus May-Cen
#   imaycen@hotmail.com
#   Version 1.0 : 23/03/2025
#

import numpy as np
import matplotlib.pyplot as plt

def simpson_rule(f, a, b, n):
    """Aproxima la integral de f(x) en [a, b] usando la regla de Simpson."""
    if n % 2 == 1:
        raise ValueError("El número de subintervalos (n) debe ser par.")
    
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)  # Puntos del intervalo
    fx = f(x)  # Evaluamos la función en esos puntos
    
    # Regla de Simpson
    integral = (h / 3) * (fx[0] + 2 * np.sum(fx[2:n:2]) + 4 * np.sum(fx[1:n:2]) + fx[n])
    
    return integral

# Función de ejemplo
def funcion(x):
    return np.sin(x)  # Cambiar esta función según el problema

# Parámetros de integración
a, b = 0, np.pi  # Intervalo
n = 10  # Número de subintervalos (debe ser par)

# Aproximación de la integral
resultado = simpson_rule(funcion, a, b, n)

# Mostrar resultado
print(f"La aproximación de la integral usando la regla de Simpson es: {resultado}")

# Gráfica de la función y la aproximación con la regla de Simpson
x_vals = np.linspace(a, b, 100)
y_vals = funcion(x_vals)

plt.plot(x_vals, y_vals, label=r"$f(x) = \sin(x)$", color="blue")
plt.fill_between(x_vals, y_vals, alpha=0.3, color="cyan", label="Área aproximada")
plt.scatter(np.linspace(a, b, n+1), funcion(np.linspace(a, b, n+1)), color="red", label="Puntos de interpolación")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.title("Aproximación de la integral con la regla de Simpson")
plt.grid()

# Guardar la figura
plt.savefig("simpson.png")
plt.show()

