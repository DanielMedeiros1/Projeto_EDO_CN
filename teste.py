import numpy as np
import matplotlib.pyplot as plt
import math

def maclaurin(x, num=10):
    soma = 0
    for k in range(num+1):
        expressao = (x ** k) / math.factorial(k)
        soma += expressao      
    return soma

x = np.linspace(0, 1, 100)
k = 10
resultado = maclaurin(x,k)
print(f"e^x ≈ {resultado[-1]}")

plt.plot(x, resultado)
plt.xlabel("x")
plt.ylabel("Valores da série para e^x")
plt.title("Maclaurin Series of e^x")
plt.grid(True)
plt.show()
