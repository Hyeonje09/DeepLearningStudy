import numpy as np
import matplotlib.pylab as plt

def relu(x):
    return np.maximum(0, x) # 두 입력 중 큰 값을 선택해 반환함.

x = np.arange(-5.0, 5.0, 0.1)
y = relu(x)

plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
