import numpy as np
import time


def matMul(a, b):
    c = np.matmul(a, b)
    return c


def basicMatMul(a, b):
    c = [[] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b)):
            sum = 0
            for k in range(len(b)):
                sum += a[i][k] * b[k][j]
            c[i].append(sum)
    return c


print("MatMul script")

m = np.genfromtxt("N-matrix-large.txt", delimiter=",", dtype=float)
st = time.time()
for i in range(10000):
    basicMatMul(m, np.transpose(m))
print(time.time() - st)

