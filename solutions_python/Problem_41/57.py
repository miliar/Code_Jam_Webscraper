#
# The Next Number
#

def get_next( n ) :
    digits = [ int( x ) for x in str( n ) ]
    is_max = True
    for i in xrange( len( digits ) - 1 ) :
        if digits[ i ] < digits[ i + 1 ] :
            is_max = False
            break
    if is_max :
        min_dig = 10
        min_i = 0
        for i in xrange( len( digits ) ) :
            if digits[ i ] > 0 and digits[ i ] < min_dig :
                min_dig = digits[ i ]
                min_i = i
        new_digits = digits[ : min_i ] + [ 0 ] + digits[ min_i + 1 : ]
        new_digits.sort()
        num = int( str( min_dig ) + str().join( [ str( x ) for x in new_digits ] ) )
        return num

    pt = -1
    for i in xrange( len( digits ) - 1, 0, -1 ) :
        if digits[ i - 1 ] < digits[ i ] :
            pt = i - 1
            break
    min_n = 10
    pt_j = -1
    if pt == 0 :
        for j in xrange( pt + 1, len( digits ) ) :
            if digits[ j ] > 0 and digits[ j ] < min_n and digits[ j ] > digits[ pt ] :
                min_n = digits[ j ]
                pt_j = j
    else :
        for j in xrange( pt + 1, len( digits ) ) :
            if digits[ j ] < min_n  and digits[ j ] > digits[ pt ] :
                min_n = digits[ j ]
                pt_j = j
    #print pt, pt_j
    new_digits = digits
    new_digits[ pt ], new_digits[ pt_j ] = new_digits[ pt_j ], new_digits[ pt ]
    new_digits[ pt + 1 : ] = sorted( new_digits[ pt + 1 : ] )
    num = int( str().join( [ str( x ) for x in new_digits ] ) )
    return num

def solve( in_name, out_name ) :
    f_in = open( in_name, "r" )
    lines = f_in.readlines()
    f_in.close()
    
    f_out = open( out_name, "w" )
    num = int( lines[ 0 ] )
    for i in xrange( 1, num + 1 ) :
        nn = int( lines[ i ].strip() )
        f_out.write( "Case #%d: %d\n" % ( i, get_next( nn ) ) )
    f_out.close()

    
solve( "B-test.in", "B-test.out" )
solve( "B-small-attempt2.in", "B-small-attempt2.out" )
solve( "B-large.in", "B-large.out" )
