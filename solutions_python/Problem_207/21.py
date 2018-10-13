#!/usr/bin/env pypy3

import sys

def solve():
    N, R, O, Y, G, B, V = map(int, input().split())
    B -= O
    Y -= V
    R -= G
    if (R < 0 or Y < 0 or B < 0):
        return "IMPOSSIBLE"
    if N == 2*(O+V+G):
        if (O != 0 and V != 0) or (V != 0 and G != 0) or (G != 0 and O != 0):
            return "IMPOSSIBLE"
        return "VY" * V + "GR" * G + "OB" * O
    f, s, l = "RBY"
    fc, sc, lc = R, B, Y
    if fc < sc:
        f, s = s, f
        fc, sc = sc, fc
    if sc < lc:
        s, l = l, s
        sc, lc = lc, sc
    if fc < sc:
        f, s = s, f
        fc, sc = sc, fc
    ans = ''
    while fc > 1:
        ans += f
        fc -= 1
        if sc > lc:
            ans += s
            sc -= 1
        else:
            ans += l
            lc -= 1
    ans += f
    fc -= 1
    if sc < lc:
        s, l = l, s
        sc, lc = lc, sc
    while sc > 1:
        ans += s + l
        sc -= 1
        lc -= 1
    ans += s
    sc -= 1
    if lc > 0:
        ans += l
        lc -= 1
    if fc != 0 or sc != 0 or lc != 0:
        return "IMPOSSIBLE"
    ans = ans.replace('R', 'G'.join('R' for _ in range(G+1)), 1)
    ans = ans.replace('Y', 'V'.join('Y' for _ in range(V+1)), 1)
    ans = ans.replace('B', 'O'.join('B' for _ in range(O+1)), 1)
    if len(ans) != N:
        return "IMPOSSIBLE"
    return ans


T = int(input())
for i in range(1, T+1):
    print("Case #%d: %s" % (i, solve()))
