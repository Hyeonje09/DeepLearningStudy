import numpy as np
import matplotlib.pylab as plt

# step function의 구성 : 아래의 함수는 넘파이 배열을 함수의 인수로 넣을 순 없음.
def step_func(x):
    if x > 0 :
        return 1
    else:
        return 0

# 이 함수에서 넘파이 배열을 함수의 인수로 넣을 수 있음.
def step_function(x):
    return np.array(x > 0, dtype=np.int32) # 전달된 원소들을 x > 0 규칙에 따라 배열로 만들어줌.

x = np.arange(-5.0, 5.0, 0.1) # -5.0 ~ 5.0 전까지 0.1 간격의 넘피이 배열을 생성함.(-5.0 ~ 4.9)
y = step_function(x) # x 배열의 원소들을 계단함수로 전달

plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
