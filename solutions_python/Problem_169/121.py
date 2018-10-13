#!/usr/bin/env python3

def diff(x, y):
    return abs(x-y) < 0.0000001

def calc(kranor, V, X):
    if len(kranor) == 0:
        return -1

    rsum = 0
    xsum = 0
    for c, r in kranor:
        rsum += r
        xsum += r * c
    x = xsum / rsum

    if diff(x, X):
        return V / rsum
    else:
        c, r = kranor[-1] if x > X else kranor[0]
        if diff(rsum, r):
            return -1
        n_x = (xsum - r * c) / (rsum - r)
        if (n_x > X and x > X) or (n_x < X and x < X):
            return calc(kranor[:-1] if x > X else kranor[1:], V, X)
        else:
            rrr = (X * (rsum - r) - (xsum - r * c)) / (c - X)
            if diff(rrr, 0):
                return calc(kranor[:-1] if x > X else kranor[1:], V, X)
            if x > X:
                kranor[-1] = (c, rrr)
            else:
                kranor[0] = (c, rrr)
            return calc(kranor, V, X)

T = int(input())

for t in range(1, T + 1):
    N, V, X = (float(x) for x in input().split())
    N = int(N)
    kranor = []
    for i in range(N):
        r, c = (float(x) for x in input().split())
        kranor.append((c, r))

    kranor.sort()

    ret = calc(kranor, V, X)
    print("Case #{}: {}".format(t, ret if ret != -1 else "IMPOSSIBLE"))


