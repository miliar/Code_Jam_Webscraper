#!/usr/bin/python

from collections import deque

def ir():
    return int(raw_input())

def ia():
    line = raw_input()
    line = line.split()
    return map(int, line)

def rsort(a): return sorted(a, reverse=True)

CNT = 0

def solve():
    ans = []
    
    N, R, O, Y, G, B, V = ia()
    a =[[R, "R"], [Y, "Y"], [B, "B"]]
    a = rsort(a)
    top = a[0]
    N -= 1

    COL = 1
    ans.append(top[1]); top[CNT] -= 1; fst = prev = top[COL]

    FLAG = 1; COL = 2
    a = [[cnt, 0, col] for cnt, col in a]
    top = a[0]; top[FLAG] = 1

    def col(e): return e[2]
    def cnt(e): return e[0]

    while N > 0:
        N -= 1
        a = rsort(a); top = a[0]
        if top[COL] == prev: top = a[1]
        ans.append(top[COL]); top[CNT] -= 1; prev = top[COL]
        if top[CNT]<0: return 'IMPOSSIBLE'

    return 'IMPOSSIBLE' if prev == fst else ''.join(ans)

T = ir()
for it in xrange(1, T + 1):
    ans = solve()
    print "Case #%d:" % it, ans
