#!/usr/bin/python

import sys
import math

def pcorr( c ):
    t = 1
    for p in c:
        t = t*p
    return t

def solve(N,K,x,c):

    tp = 0

    # begin with small where N=K

    # begin to increase most likely to fail in greedy fashion

    cc = sorted(c)

    t = 1
    for i,a in enumerate(cc):

        n = 0
        if ( i == len(cc)-1 ):
            n = 1
        else:
            n = cc[i+1]

        if ( (n-a)*t >= x ):
            cc = [ a + x/t for i in range( t ) ] + [ cc[t+i] for i in range(N-t) ]
            break
        else:
            cc = [ n for i in range( t ) ] + [ cc[t+i] for i in range(N-t) ]


        x = x-((n-a)*t)
        t = t + 1

    return pcorr(cc)
    
testcases = int( sys.stdin.readline() )
for i in range( testcases ):

    data = [ int(x) for x in sys.stdin.readline().strip().split() ]
    N = data[0]
    K = data[1]

    data = [ float(x) for x in sys.stdin.readline().strip().split() ]
    x = data[0]

    c = [ float(j) for j in sys.stdin.readline().strip().split() ]


    print( "Case #{}: {}".format( i+1, solve(N,K,x,c)) )


