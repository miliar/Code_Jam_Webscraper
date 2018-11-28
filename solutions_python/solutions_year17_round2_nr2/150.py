#!/usr/bin/env python3

import itertools

def mix(a, b):
    L = []
    for x, y in itertools.zip_longest(a, b):
        if x is not None: L.append(x)
        if y is not None: L.append(y)
    return L

def solve(N, R, O, Y, G, B, V):
    if R == G and R+G == N: return "RG" * R
    if Y == V and Y+V == N: return "YV" * Y
    if B == O and B+O == N: return "BO" * B
    if G > 0 and R < G+1: return "IMPOSSIBLE"
    if V > 0 and Y < V+1: return "IMPOSSIBLE"
    if O > 0 and B < O+1: return "IMPOSSIBLE"
    rs = R > 0 and ['R' for i in range(R-G-1)] + ['R' + 'GR' * G] or []
    ys = Y > 0 and ['Y' for i in range(Y-V-1)] + ['Y' + 'VY' * V] or []
    bs = B > 0 and ['B' for i in range(B-O-1)] + ['B' + 'OB' * O] or []
    xs, ys, zs = map(lambda p: p[1],
                     sorted([(len(rs), rs), (len(ys), ys), (len(bs), bs)]))
    if len(zs) > len(xs) + len(ys): return "IMPOSSIBLE"
    result = "".join(mix(ys, reversed(mix(zs, xs))))
    return result

tests = int(input())
for test in range(tests):
    N, R, O, Y, G, B, V = map(int, input().split())
    result = solve(N, R, O, Y, G, B, V)
    print("Case #{}: {}".format(1+test, result))
