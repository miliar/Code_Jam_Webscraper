import collections
import heapq

def read_line():
    return raw_input().strip()

def read_words():
    return read_line().split()

def read_integer():
    return int( read_line() )

def read_integers():
    return [ int( x ) for x in read_words() ]

def fare( start, end, count ):
    n = end - start
    return count*( N*n - n*( n -1 )/2 )

T = read_integer()
for t in range( T ):
    N, M = read_integers()
    routes = []
    reference = 0
    entrances = collections.defaultdict( int )
    #destinations = collections.defaultdict( int )
    sequence = []
    for m in range( M ):
        o, e, p = read_integers()
        sequence.append( ( o, -p ) )
        sequence.append( ( e, p ) )
        reference += fare( o, e, p )
    sequence.sort()
    cost = 0
    boarding = True
    for station, p in sequence:
        if p < 0:
            entrances[ station ] -= p
        else:
            while p > 0:
                board = max( entrances )
                count = min( entrances[ board ], p )
                if count == entrances[ board ]:
                    del entrances[ board ]
                else:
                    entrances[ board ] -= count
                cost += fare( board, station, count )
                p -= count
    print 'Case #%i:' % ( t + 1 ), reference - cost
