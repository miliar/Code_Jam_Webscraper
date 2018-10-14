import sys

def read_integer_line():
    row = [ int( x ) for x in sys.stdin.readline().split() ]
    if len( row ) == 1:
        return row[ 0 ]
    else:
        return row

T = read_integer_line()

for index in range( T ):
    N, K = read_integer_line()
    print "Case #%i:" % ( index + 1 ), "OFF" if ( K + 1 ) % 2**N else "ON"
