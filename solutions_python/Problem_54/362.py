import sys

def read_integer_line():
    row = [ int( x ) for x in sys.stdin.readline().split() ]
    if len( row ) == 1:
        return row[ 0 ]
    else:
        return row

def GCD( a, b ):
    while b:
       a, b = b, a % b
    return a

C = read_integer_line()
for index in range( C ):
    T = read_integer_line()
    N = T.pop( 0 )
    offset = min( T )
    T = [ t - offset for t in T if t != offset ]
    period = reduce( GCD, T )
    elapsed = ( max( T ) + offset ) % period
    print "Case #%i:" % ( index + 1 ), period - elapsed if elapsed else 0
