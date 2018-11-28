import sys

T = int( raw_input( ) )
for i in xrange( T ) :
    A, B = map( int, raw_input( ).split( ) )
    r = 0
    for N in xrange( A, B + 1 ) :
        n = str( N )
        l = len( n )
        s = set( )
        for j in xrange( 1, l ) :
            p = n[ j : l ] + n[ 0 : j ]
            P = int( p )
            if N < P and P <= B :
                s.add( p )
        r += len( s )
    print 'Case #' + str( i + 1 ) + ': ' + str( r )