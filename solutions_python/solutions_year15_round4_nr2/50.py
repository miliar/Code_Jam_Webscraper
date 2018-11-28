#!/usr/bin/python3
# -*- coding: utf-8 -*-

def solve():
    n, Vr, Xr = input().split()
    n = int(n)
    Vr = float(Vr)
    Xr = float(Xr)
    V = [0] * n
    X = [0] * n
    for i in range (n):
        V[i], X[i] = map(float, input().split())
    if n == 1:
        if X[0] != Xr:
            return "IMPOSSIBLE"
        else:
            return Vr / V[0]
    if n == 2:
        if X[0] == X[1] == Xr:
            return Vr / (V[0] + V[1])
        if X[0] == Xr:
            return Vr / (V[0])
        if X[1] == Xr:
            return Vr / (V[1])
        if X[0] > X[1]:
            X[0], X[1] = X[1], X[0]
            V[0], V[1] = V[1], V[0]
        if X[0] >= Xr or X[1] <= Xr:
            return "IMPOSSIBLE"
        # Теперь X[0] < Xr < X[1], двоичным поиском смешиваем
        left = 0
        right = Vr
        # Это сколько мы берем воды из первого крана
        # В left температура результата больше требуемой, в right - меньше требуемой
        while right - left >= 1e-12:
            m = (left + right) / 2
            V0 = m
            V1 = Vr - m
            res = (V0 * X[0] + V1 * X[1]) / Vr;
            if res > Xr:
                left = m
            else:
                right = m
        x = (left + right) / 2
        return max(x / V[0], (Vr - x) / V[1])

T = int(input())
for t in range(1, T + 1):
    print("Case #" + str(t) + ":", solve())

