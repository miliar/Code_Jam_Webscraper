#!/usr/bin/env python3

import sys

T = int(sys.stdin.readline().strip())

def subsolve(c, v, best):
    print("SS: {} {}".format(c, v))
    if X - c <= C:
        return (X-c) / v

    # try buy the farm
    tb = (C - c) / v

    # try wait
    e2 = (X - c) / v

    if e2 <= tb:
        return e2
    else:
        e1 = tb + subsolve(c + tb * v - C, v + F)
        return min(e1, e2)

def solve(C, F, X):
    c = 0
    v = 2
    prevT = X / 2
    psum = 0
    i = 1
    while True:
        psum += C / (2 + (i-1)*F)
        t = psum + X / (2 + i*F)
        if t > prevT:
            # print("{} needed".format(i-1))
            return prevT
        prevT = t
        i += 1


for t in range(T):
    C, F, X = [float(_) for _ in sys.stdin.readline().strip().split()]

    res = solve(C, F, X)
    print("Case #{}: {}".format(t+1, res))

