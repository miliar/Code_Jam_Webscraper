#!/usr/bin/python

import sys

# Will need logish solution for 10**18
# divide into two intervals when putting a new in
# keep collection of the intervalls of different sizes
# use up a whole size klass of intervalls simultaneously
# classes will grow in size exponentially, and we need not
# store a very large amount of classes simultaneously ( logarithmic? )
# use dict to store the size class; and after finishing one add two 
# new ones, and search through them all for smallest ( log**2 is ok )

#find the next size to handle ( should always be the one with largest size (we pick middle) )
def findBest( sizelist ):
    return max( sizelist )

def divide( size ):
    s = size - 1
    if ( s % 2 == 0 ):
        return s / 2, s / 2
    else:
        return s/2, s/2 + 1

def solve( n, k ):

    sizes = dict()
    sizes[ n ] = 1

    l , r = 0,0

    while ( k > 0 ):
        size = findBest( sizes.keys() )
        amount = sizes[size]

        k -= amount
        del sizes[size]

        l, r = divide( size )
        
        if ( sizes.has_key(l) ):
            sizes[ l ] += amount
        else:
            sizes[ l ] = amount

        if ( sizes.has_key(r) ):
            sizes[ r ] += amount
        else:
            sizes[ r ] = amount

    return max( [ l, r ] ), min( [ l, r ] )


testcases = int( sys.stdin.readline() )
data = [ [ int(a) for a in x.strip().split() ] for x in sys.stdin.readlines() ]
for i in range( testcases ):
    x, z = solve( data[i][0], data[i][1] )
    print( "Case #{}: {} {}".format( i+1, x, z ) )

