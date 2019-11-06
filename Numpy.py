import numpy as np
# 1.从python的基础数据转化
a = [1,2,3,4]
x1 = np.array(a)
print(x1)
# 2.通过numpy内生的函数生成
x = np.arange(11)
print(x)
c = np.arange(11)
print(c)
d = np.random.randint(1,100,10)
print(np.mean(d))
print(d.mean())