import numpy as np
import matplotlib.plot as plt

x = np.linspace(0, 2*np.pi)
y = np.sin(x)

plt.plot(x, y, label='sin(x)')
plt.title('sin(x)')
plt.xlable('x')
plt.ylable('y')
plt.legend()
plt.show()