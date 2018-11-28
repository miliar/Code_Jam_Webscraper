import sys

def readline():
    return sys.stdin.readline().strip()

T = int( readline() )

sequence = range( 36 )
sequence[ 0 : 2 ] = [ 1, 0 ]
for t in range( T ):
    number = readline()
    base = max( len( set( number ) ), 2 )
    lookup = {}
    decoded = []
    for digit in number:
        decoded.append( lookup.setdefault( digit, sequence[ len( lookup ) ] ) )
    #print decoded, base
    print 'Case #%i: %i' % ( t + 1, int( ''.join( str( x ) for x in decoded ), base ) )
