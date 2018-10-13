#!/usr/bin/python

import sys

# find invalid order and say that everything after is nines.
def solve( n ):

    s = str(n)
    l = len(s)
    ls = list(s)

    for e, i in enumerate( range( l-1, 0, -1 ) ):
#        print i, e, n
        if  ( ls[i] < ls[i-1] ):
            return solve( ( n / 10**e ) - 1 ) + "9"*e  

    return s

testcases = int( sys.stdin.readline() )
data = [ int(x.strip()) for x in sys.stdin.readlines() ]
for i in range( testcases ):
    print( "Case #{}: {}".format( i+1, solve(data[i])) )



