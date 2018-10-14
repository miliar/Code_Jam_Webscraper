#
# Decision Tree
#

def make_tree( s ) :
    ss = s.strip()
    #print ss
    assert( ss[ 0 ] == "(" )
    c = 1
    while str.isspace( ss[ c ] ) : c += 1
    cc = c
    while str.isdigit( ss[ cc ] ) or ss[ cc ] == "." : cc += 1
    coeff = float( ss[ c : cc ] )
    
    c = cc
    while str.isspace( ss[ c ] ) : c += 1
    if ss[ c ] == ")" : return ( c + 1, coeff, None )
    
    cc = c
    while not str.isspace( ss[ cc ] ) : cc += 1
    feature = ss[ c : cc ]
    
    c = cc
    while str.isspace( ss[ c ] ) : c += 1
    
    #print "1: ", ss[ c : ]
    ( i, cf1, node1 ) = make_tree( ss[ c : ] )
    c += i
    #print "2: ", ss[ c : ]
    ( i2, cf2, node2 ) = make_tree( ss[ c : ] )
    c += i2 + 1
    
    #print ">>>", ss[ c : ]
    while str.isspace( ss[ c ] ) : c += 1
    assert( ss[ c ] == ")" )
    
    return ( c + 1, coeff, ( feature, ( cf1, node1 ), ( cf2, node2 ) ) )

def solve( in_name, out_name ) :
    f_in = open( in_name, "r" )
    lines = f_in.readlines()
    f_in.close()

    f_out = open( out_name, "w" )
    N = int( lines[ 0 ].strip() )
    l = 1
    for i in xrange( N ) :
        L = int( lines[ l ].strip() )
        l += 1
        tree_str = ""
        for j in xrange( L ) :
            tree_str += lines[ l ].strip() + " "
            l += 1
        A = int( lines[ l ].strip() )
        l += 1
        animals = []
        for j in xrange( A ) :
            an = lines[ l ].strip().split( " " )
            features = set()
            for k in xrange( 2, len( an ) ) :
                features.add( an[ k ] )
            animals.append( ( an[ 0 ], features ) )
            l += 1

        f_out.write( "Case #%d:\n" % ( i + 1 ) )
        tree = make_tree( tree_str )
        for ( animal, features ) in animals :
            ff = tree
            p = ff[ 1 ]
            ff = ff[ 2 ]
            while ff :
                ( feature, ff1, ff2 ) = ff
                if feature in features :
                    p *= ff1[ 0 ]
                    ff = ff1[ 1 ]
                else :
                    p *= ff2[ 0 ]
                    ff = ff2[ 1 ]
            f_out.write( "%.7f\n" % ( p ) )
    f_out.close()


solve( "A-test.in", "A-test.out" )
solve( "A-small-attempt0.in", "A-small-attempt0.out" )
solve( "A-large.in", "A-large.out" )
