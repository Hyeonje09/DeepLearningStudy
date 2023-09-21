# 논리 회로 퍼셉트론 구현
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.8 # AND게이트의 매개변수
    # w1, w2, theta = 0.7, 0.7, 0.5 # OR게이트의 매개변수
    # w1, w2, theta = -0.5, -0.5, -0.8 # NAND 게이트의 매개변수
    
    y = x1*w1 + x2*w2
    
    if y <= theta:
        return 0
    elif y > theta:
        return 1
    
print(AND(0, 0))
print(AND(0, 1))
print(AND(1, 0))
print(AND(1, 1))