#!/usr/bin/python3
# -*- coding: utf-8 -*-

def solve():
    line = input().split()
    N = int(line[0])
    V = float(line[1])
    X = float(line[2])
    R = []
    C = []
    for _ in range(N):
        r, c = map(float, input().split())
        R.append(r)
        C.append(c)
    res = 0
    if min(C) > X + 1e-6 or max(C) < X - 1e-6:
        return "IMPOSSIBLE"
    if N == 1:
        res = V / R[0]
    elif N == 2:
        if abs(C[0] - C[1]) < 1e-6:
            res = V / (R[0] + R[1])
        else:
            V0 = (X * V - V * C[1]) / (C[0] - C[1])
            V1 = V - V0
            res = max(V0 / R[0], V1 / R[1])
    else:
        return "IMPOSSIBLE"
    return "%.10f" % res

if __name__=="__main__":
    T = int(input())
    for t in range(1, T+1):
        print("Case #%d:" % t, solve())

