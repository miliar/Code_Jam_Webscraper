import math

def stall(n, k):
    frac = (n-1) / 2
    mi = math.floor(frac)
    ma = math.ceil(frac)
    if k==1:
        return ma, mi
    else:
        k -= 1
        if k % 2 == 1:
            return stall(ma, (k+1)/2)
        else:
            return stall(mi, k/2)

import sys

n = (int) (sys.stdin.readline().strip())
for i in range (1, n+1):
    data = [int(x) for x in sys.stdin.readline().split(' ')]
    ma, mi = stall(data[0], data[1])
    print(f"Case #{i}: {ma} {mi}")
