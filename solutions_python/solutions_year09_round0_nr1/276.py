#
# Alien Language
#

def count_matches( pattern, words ) :
    letters = []
    i = 0
    while i < len( pattern ) :
        if pattern[ i ] == "(" :
            i += 1
            ls = set()
            while pattern[ i ] != ")" :
                ls.add( pattern[ i ] )
                i += 1
            letters.append( ls )
        else :
            letters.append( set( [ pattern[ i ] ] ) )
        i += 1

    count = 0
    for w in words :
        match = True
        for i in xrange( len( w ) ) :
            if w[ i ] not in letters[ i ] :
                match = False
                break
        if match : count += 1
    return count

def solve( in_name, out_name ) :
    f_in = open( in_name, "r" )
    lines = f_in.readlines()
    f_in.close()

    f_out = open( out_name, "w" )
    ( L, D, N ) = [ int( x ) for x in lines[ 0 ].strip().split( " " ) ]

    words = []
    l = 1
    for i in xrange( D ) :
        words.append( lines[ l ].strip() )
        l += 1
    test_cases = []
    for i in xrange( N ) :
        test_cases.append( lines[ l ].strip() )
        l += 1
    
    for i in xrange( N ) :
        f_out.write( "Case #%d: %d\n" % ( i + 1, count_matches( test_cases[ i ], words ) ) )
    f_out.close()


solve( "A-test.in", "A-test.out" )
solve( "A-small-attempt0.in", "A-small-attempt0.out" )
solve( "A-large.in", "A-large.out" )
