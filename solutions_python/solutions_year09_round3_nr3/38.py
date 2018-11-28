#import collections
import sys

def readline():
    return sys.stdin.readline().strip()

cache = {}

N = int( readline() )


def minimum_cost( strip ):
    left, right, candidates = strip
    lowest_cost = P**2 + 1
    for candidate in candidates:
        cost = 0
        lower = tuple( c for c in candidates if c < candidate )
        if lower:
            strip = ( left, candidate - 1, lower )
            cost += cache.setdefault( strip, minimum_cost( strip ) )
        higher = tuple( c for c in candidates if c > candidate )
        if higher:
            strip = ( candidate + 1, right, higher )
            cost += cache.setdefault( strip, minimum_cost( strip ) )
        if cost < lowest_cost:
            lowest_cost = cost
    return right - left + lowest_cost

for n in range( N ):
    P, Q = ( int( x ) for x in readline().split() )
    releases = tuple( int( x ) for x in readline().split() )
    cache.clear()
    print 'Case #%i: %i' % ( n + 1, minimum_cost( ( 1, P, releases ) ) )
