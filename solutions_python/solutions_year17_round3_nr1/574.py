#!/usr/bin/python

from collections import deque
from itertools   import combinations as comb
from math        import pi

def ir(): return int(raw_input())
def ia(): return map(int, raw_input().split())

def solve():
    n, k = ia()
    D = []
    for i in xrange(n): D.append(tuple(ia()))
    D.sort(reverse = True)

    ma = 0
    for i in xrange(n):
        H = D[i] # head
        T = D[i + 1 : ] # tail
        if len(T) < k - 1: break
        r, h = H; a = r*r + 2*r*h
        
        T = [2*t[0]*t[1] for t in T]
        T.sort(reverse = True)
        a += sum(T[ : k - 1])
        ma = max(a, ma)

    return pi*ma

    #return pi*max([area(c) for c in comb(D, K)])

T = ir()
for it in xrange(1, T + 1):
    ans = solve()
    print "Case #%d:" % it , ans
