#!/bin/env python2
import sys

def GT(D):
    def T(KS):
        K, S = KS
        return float(D-K)/S
    return T

def solve(D, N, KS):
    T = GT(D)
    return float(D)/max( map( T, KS ) )

def main():
    f = open( sys.argv[1] )
    T = int( f.next().strip() )
    for n in range(T):
        D, N = map(int, f.next().strip().split())
        KS = [ map(int, f.next().strip().split()) for i in range(N) ]
        print "Case #{0}: {1:.6f}".format( n+1, solve(D, N, KS) )

main()

