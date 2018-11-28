import sys

# sys.stdin.readline()
for cases in xrange( int ( sys.stdin.readline() ) ):
    D, N = map( int, sys.stdin.readline().split() )
    t = 0
    for i in xrange( N ):
        K, S = map( int, sys.stdin.readline().split() )
        t = max( ( D - K ) / ( S * 1.0 ), t )
    print "Case #%d: %.6f"%(cases + 1, D / t )
