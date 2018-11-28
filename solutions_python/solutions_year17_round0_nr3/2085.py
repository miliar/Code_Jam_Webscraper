#!/bin/env python2
import sys, heapq

"""
def fit( span ):
    x, y = span
    z = (x+y-1)/2
    return z, z-x, y-z-1
    

0 1
0 0 0

0 2
0 0 1 *     1 1 0

0 3
0 0 2       1 1 1 *     2 2 0

0 4
0 0 3       1 1 2 *     2 2 1       3 3 0

3 7
3 0 3       4 1 2 *     5 2 1       6 3 0

def show_stalls( stalls, N ):
    x = [ 1 ] * N
    for a, b in stalls:
        x[a:b] = [0]*(b-a)
    print " "*8 + "".join( map( "{0: 3}".format, x ) )

def show_slot( slot, Ls, Rs ):
    print " "*5 + "   "*slot + "{0: 3}  ^{1: 3}".format( Ls, Rs )


def inc( stalls, N ):
    show_stalls(stalls, N)
    i, span = max( enumerate(stalls), key=lambda x: x[1][1]-x[1][0] )
    slot, Ls, Rs = fit(span)
    show_slot( slot, Ls, Rs )
    replace = []
    if Ls: replace.append( (span[0], slot) )
    if Rs: replace.append( (slot+1, span[1]) )
    stalls[i:i+1] = replace
"""

def ins( slots ):
    #print "slots:", slots
    n = -heapq.heappop( slots )
    Ls = (n-1)/2
    Rs = n - 1 - Ls
    #print Ls, Rs
    if Ls: heapq.heappush( slots, -Ls )
    if Rs: heapq.heappush( slots, -Rs )
    return max(Ls, Rs), min(Ls, Rs)


def solve(N, K):
    #stalls = [ (0, N) ]
    slots = [ -N ]
    for i in range(K):
        a = ins( slots )
    return a

def main():
    f = open( sys.argv[1] )
    #f = sys.stdin
    T = int( f.next().strip() )
    for n, line in enumerate(f):
        N, K = map(int, line.strip().split() )
        print "Case #{0}: {1} {2}".format( n+1, *solve(N,K) )

main()
