#!/usr/bin/python

# google code jam - c.durr - 2011

# House of Kittens
# colorier graphe planaire
# complexite O(N^2) -- solution du competiteur rng..58


try:
    import psyco
except:
    pass

from math      import *

def readint():    return int(raw_input())
def readarray(f): return map(f, raw_input().split())



def solve(N, E):
    return C, color, K


for test in range(readint()):
    X, S, R, t, N = readarray(int)
    runway = []
    for _ in range(N):
        Bi,Ei,wi = readarray(int)
        runway.append((wi,float(Ei-Bi)))
    runway.sort()
    L = X - sum([li for (wi,li) in runway])
    runway.append((0,L))
    runway.sort()
    y = 0
    for (wi,li) in runway:
        if t>0:
            a = min(t,li/(wi+R))
            y += a
            li -= (wi+R)*a
            t -= a
        if li>0:
            a = li/(wi+S)
            y += a

    print "Case #%i:"% (test+1), y
    
    
    
