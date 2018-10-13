import sys
import numpy as np

filename = sys.argv[1]
f = open(filename)

cases = int(f.next())


class T:
    def __init__(self,a,b,c):
        self.st = a
        self.ed = b
        self.w = c

def solve():
    N,C,M = map(int, f.next().split())
    a = [[,],[,]]

    for i in range(M):
        p,q = map(int, f.next().split())
        a[q].append(p)
        

    if N == 1:
        return "%d"%M

    k = max(len(a[0]), len(a[1]))
    c = [m.count(1) for m in a]

    r = c[0] + c[1]

    k1 = len(a[0]) - r
    k2 = len(a[1]) - r

    pp = 0
    for j in range(2000):
        u1 = a[0].count(j) - c[1]
        u2 = a[1].count(j) - c[0]
        pp = max(pp, u1+u2-max(k1,k2))

    if r >= len(a[0]) || r >= len(a[1]):
        pp = 0

    return "%d %d"%(max(r, k), pp)

for i in range(1, cases+1):
    print("Case #%d: %s"%(i, solve()))