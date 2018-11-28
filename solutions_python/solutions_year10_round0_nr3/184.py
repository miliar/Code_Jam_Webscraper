import sys

def read_integer_line():
    return [ int( x ) for x in sys.stdin.readline().split() ]


T, = read_integer_line()
for t in range( T ):
    R, k, N  = read_integer_line()
    G = read_integer_line()
    if sum( G ) <= k:
        total = R*sum( G )
    else:
        total = 0
        #rides = 0
        index = 0
        rides_cache = N*[ 0 ]
        index_cache = N*[ 0 ]
        for r in range( R ):
            rides = 0
            if rides_cache[ index ]:
                total += rides_cache[ index ]
                index = index_cache[ index ]
            else:
                start_index = index
                while rides + G[ index ] <= k:
                    rides += G[ index ]
                    index = ( index + 1 ) % N
                total += rides
                rides_cache[ start_index ] = rides
                index_cache[ start_index ] = index
    print "Case #%i:" % ( t + 1 ), total
