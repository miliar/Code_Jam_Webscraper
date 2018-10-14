from sys import *
import math

def readints():
    return list(map(int, stdin.readline().split()))

def isTidy(n):
    n = str(n)

    for i in range(1, len(n)):
        if n[i] < n[i - 1]:
            return False

    return True

T, = readints()

for i in range(T):
    N, = readints()

    for found in range(N, 0, -1):
        if isTidy(found):
            break

    print("Case #{}: {}".format(i + 1, found))
