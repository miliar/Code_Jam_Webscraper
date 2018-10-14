#
# Welcome to Code Jam
#

def count_ways( string, pattern ) :
    if len( pattern ) == 0 : return 1

    l = pattern[ 0 ]
    count = 0
    for i in xrange( len( string ) ) :
        if string[ i ] == l :
            count += count_ways( string[ i + 1 : ], pattern[ 1 : ] )
    return count

def solve( in_name, out_name ) :
    f_in = open( in_name, "r" )
    lines = f_in.readlines()
    f_in.close()

    f_out = open( out_name, "w" )
    N = int( lines[ 0 ].strip() )
    strings = lines[ 1 : ]

    for i in xrange( N ) :
        f_out.write( "Case #%d: %04d\n" % ( i + 1, count_ways( strings[ i ], "welcome to code jam" ) % 10000 ) )
    f_out.close()


solve( "C-test.in", "C-test.out" )
solve( "C-small-attempt0.in", "C-small-attempt0.out" )
#solve( "A-large.in", "A-large.out" )
