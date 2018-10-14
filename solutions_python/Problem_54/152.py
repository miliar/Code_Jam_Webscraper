#!/usr/bin/env python
from scanf import *
dbg = False
def euclid(a,b):
    if a < b:
        e = euclid(b,a)
        return (e[1],e[0])
    if b == 0:
        return (1,0)
    e = euclid(b,a%b)
    return (e[1],e[0]-(a/b)*e[1])

def gcd(a,b):
    if dbg:print("gcd(%d,%d)"%(a,b))
    if a < b:
        return gcd(b,a)
    if b == 0:
        return a
    return gcd(b,a%b)

def lcd(a,b):
    return a*b/gcd(a,b)

def solveCase(cas):
    n = scanf("%d")[0]
    t = []
    g = 0
    for i in range(n):
        t.append(scanf("%d")[0])
    for i in t:
        for j in t:
            g = gcd(abs(i-j),g)
    if dbg: print("g:"+str(g))
    res = (g - (t[0]%g))%g
    print("Case #"+str(cas)+": "+str(res))

if __name__ == "__main__":
    tests = scanf("%d")[0]
    for i in range(tests):
        solveCase(i+1)
