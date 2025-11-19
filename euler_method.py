# euler_method.py
import numpy as np
import matplotlib.pyplot as plt

# Example ODE: dy/dx = x + y, with y(0)=1
def f(x, y):
    return x + y

def euler(x0, y0, h, n):
    x = np.zeros(n + 1)
    y = np.zeros(n + 1)
    x[0], y[0] = x0, y0

    for i in range(n):
        y[i + 1] = y[i] + h * f(x[i], y[i])
        x[i + 1] = x[i] + h

    return x, y

if __name__ == "__main__":
    x0 = 0.0
    y0 = 1.0
    h = 0.1
    n = 50

    x, y = euler(x0, y0, h, n)

    plt.plot(x, y, marker='o')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Solution using Euler's Method")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
