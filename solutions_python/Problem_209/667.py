#!/bin/env python2
import sys
from math import pi
from itertools import combinations

def hh( RH, K ):
    if K == 0:
        return 0
    if K < 0 or len(RH) < K:
        print "!!!"
        return -100000000000
    if K == 1:
        return max( ( 2*rh[0] * rh[1] for rh in RH ) )
    a1 = 2*RH[0][0] * RH[0][1] + hh( RH[1:], K-1 )
    a2 = hh( RH[1:], K )
    return max(a1, a2)

def rr( rh ):
    r, h  = rh
    return r*r + 2*r*h

def solve(N, K, RH):
    RH.sort( reverse = True )
    a = [ (rr( RH[i] ), hh( RH[i:], K-1 )) for i in range(N) ]
    a = [ (x+y, x, y) for x, y in a ]
    print "="*20
    print N, K, RH
    print a
    return pi*max(a)[0]

def s2(RH):
    rh = max(RH)
    return rh[0]*rh[0] + sum( (2*r*h for r, h in RH))

def solve2(N, K, RH):
    a = [ (s2(i)*pi, i) for i in combinations(RH, K) ]
    return max(a)[0]

x = [[899682, 708602], [778919, 325202], [692238, 810927], [609115, 749994], [552684, 859155], [371280, 626301], [361928, 336072], [89429, 756749]]

solve2( 8, 5, x )


def main():
    f = open( sys.argv[1] )
    T = int( f.next().strip() )
    for n in range(T):
        N, K = map(int, f.next().strip().split())
        RH = [ map(int, f.next().strip().split()) for i in range(N) ]
        print "Case #{0}: {1:.9f}".format( n+1, solve2(N, K, RH) )

main()

