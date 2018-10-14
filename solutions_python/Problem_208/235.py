#!/bin/env python2
import sys

def GT(D):
    def T(KS):
        K, S = KS
        return float(D-K)/S
    return T

def solve(ES, Dij, x, y):
    e, s = ES[x]
    d = Dij[x][x+1] 
    if d > e:
        return -1
    t = float(d) / s
    if x+1 == y:
        #print "just one step from {0} to {1}: t={2}", x, y, t
        return t
    a = solve(ES, Dij, x+1, y)
    #print "a={0}".format(a)
    if e-d >= Dij[x+1][x+2]:
        tmp = ES[x+1]
        ES[x+1] = e-d, s
        b = solve(ES, Dij, x+1, y)
        #print "b={0}".format(b)
        ES[x+1]=tmp
        if b > 0 and b < a:
            a = b
    return t+a

def main():
    f = open( sys.argv[1] )
    T = int( f.next().strip() )
    for n in range(T):
        N, Q = map(int, f.next().strip().split())
        ES = [ map(int, f.next().strip().split()) for i in range(N) ]
        Dij = [ map(int, f.next().strip().split()) for i in range(N) ]
        UV = [ map(int, f.next().strip().split()) for i in range(Q) ]
        print "Case #{0}: {1:.6f}".format( n+1, solve(ES, Dij, 0, N-1) )

main()

