import sys
from fractions import gcd
from math import ceil

d = {}

def solve( n, origValue):
    if n <= 1:  return 
    left = right = n / 2
    if ( n % 2 == 0 ):  left -= 1
    d[ origValue ].append( ( right, left ) )

    if left in d:   d[origValue] += d[left]
    else:           solve( left, origValue )

    if right in d:  d[origValue] += d[right]
    else:           solve( right, origValue )

def solve1( N, K ):
    if N in d:
        L = d[N]
        if K > len(L):  return 0,0
        return L[K-1]

    d[N] = list()
    solve( N, N )
    d[N].sort( reverse = True )
    L = d[N]
    if K > len(L):  return 0,0
    return L[K-1]

for cases in xrange( int( sys.stdin.readline() ) ):
    N, K = map( int, sys.stdin.readline().strip().split() )
    x,y = solve1( N, K )
    print "Case #%d: %d %d"%( cases + 1, x, y )
    
