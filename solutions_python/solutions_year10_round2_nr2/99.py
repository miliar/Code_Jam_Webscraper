import sys

def read_integer():
    return int( sys.stdin.readline() )

def read_integer_line():
    return [ int( x ) for x in sys.stdin.readline().split() ]

def read_string():
    return sys.stdin.readline().strip()

C = read_integer()

for c in range( C ):
    print 'Case #%i:' % ( c + 1 ),
    N, K, B, T = read_integer_line()
    X = read_integer_line() # sorted
    if K == 0:
        print 0
    V = [ float( x ) for x in read_integer_line() ]
    chicks = zip( X, V )
    arrivals = [ ( B - x )/v for x, v in chicks ]
    if sum( 1 if t <= T else 0 for t in arrivals ) < K:
        print 'IMPOSSIBLE'
        continue
    cum = 0
    blocks = [ None ]*N
    for index in reversed( range( N ) ):
        cum += 1 if arrivals[ index ] > T else 0
        blocks[ index ] = cum
    swaps = 0
    count = 0
    for index in reversed( range( N ) ):
        if arrivals[ index ] <= T:
            count += 1
            swaps += blocks[ index ]
            if count == K:
                print swaps
                break
