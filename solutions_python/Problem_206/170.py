#!/usr/bin/python

import sys


def solve( N,D,K,S ):

    slowesttime = 0

    for h in range( N ):
        time = float(D-K[h]) / S[h]
        if ( time > slowesttime ):
            slowesttime = time

    return float(D) / float(slowesttime) 

    

testcases = int( sys.stdin.readline() )
for i in range( testcases ):

    data = [ int(x) for x in sys.stdin.readline().strip().split() ]
    D = data[0]
    N = data[1]
    K = []
    S = []
    for j in range(N):
        data = [ int(x) for x in sys.stdin.readline().strip().split() ]
        K.append( data[0] )
        S.append( data[1] )

    print( "Case #{}: {}".format( i+1, solve(N,D,K,S)) )



