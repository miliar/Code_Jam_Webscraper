#!/usr/bin/python

import sys
import math

def flatS( R ):
    return math.pi * R**2

def highS( R, H ):
    return math.pi * R * H * 2

def solve(N,K,R,H):

    # only largest pancake top matters
    # rest us sum of heights
    # n**2 solution is good
    # order pancakes by width and then check best stack for each width - no
    # use simple greed to select highest most value pancake until only last left
    # then greed needs to care about flat also

    hs = [ [ highS(R[i],H[i]), R[i], H[i], flatS( R[i] ) ] for i in range(N) ]

    hso = sorted( hs, key= lambda v: v[0] )

    # take K-1 from sort
    # take last one making this maximum ( sum value + rad value of biggest + h value of biggest )
    # need to check and see if some last has higher rad than already chosen, else take next from sort

    mv = 0
    if ( K != 1 ):
        chos = hso[-K+1:]

        mc = max( chos, key= lambda v:v[1] )
        fmc = flatS( mc[1] )

        vcho = sum( x[0] for x in chos  )


        left = hso[:N-K+1]
        for e in left:
            if ( e[1] > mc[1] ):
                v = vcho + highS( e[1], e[2] ) + flatS( e[1] )
                if ( v> mv ):
                    mv = v
            else:
                # not larger
                v = vcho + highS( e[1], e[2] ) + fmc
                if ( v> mv ):
                    mv = v
    else:
        for e in hso:
            mv = max( mv, highS( e[1],e[2] ) + flatS( e[1] ) )

    return mv
    
testcases = int( sys.stdin.readline() )
for i in range( testcases ):

    data = [ int(x) for x in sys.stdin.readline().strip().split() ]
    N = data[0]
    K = data[1]

    R = []
    H = []
    for j in range(N):
        data = [ int(x) for x in sys.stdin.readline().strip().split() ]
        R.append( data[0] )
        H.append( data[1] )


    print( "Case #{}: {}".format( i+1, solve(N,K,R,H)) )


