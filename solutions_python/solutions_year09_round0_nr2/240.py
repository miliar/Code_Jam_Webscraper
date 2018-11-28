#
# Watersheds
#

def get_min_neigh( field, x, y ) :
    neighs = []
    sx, sy = len( field[ 0 ] ), len( field )
    if x > 0 : neighs.append( field[ y ][ x - 1 ] )
    if x < sx - 1 : neighs.append( field[ y ][ x + 1 ] )
    if y > 0 : neighs.append( field[ y - 1 ][ x ] )
    if y < sy - 1 : neighs.append( field[ y + 1 ][ x ] )
    if len( neighs ) == 0 : return None
    mm = min( neighs )
    if y > 0 and mm == field[ y - 1 ][ x ] : return ( field[ y - 1 ][ x ], 0, -1 )
    if x > 0 and mm == field[ y ][ x - 1 ] : return ( field[ y ][ x - 1 ], -1, 0 )
    if x < sx - 1 and mm == field[ y ][ x + 1 ] : return ( field[ y ][ x + 1 ], 1, 0 )
    if y < sy - 1 and mm == field[ y + 1 ][ x ] : return ( field[ y + 1 ][ x ], 0, 1 )

def make_sheds( field ) :
    sx, sy = len( field[ 0 ] ), len( field )
    sheds = [ [ None ] * sx for x in xrange( sy ) ]
    for y in xrange( sy ) :
        for x in xrange( sx ) :
            min_neigh = get_min_neigh( field, x, y )
            if min_neigh :
                ( m, dx, dy ) = min_neigh
                if m < field[ y ][ x ] :
                    sheds[ y ][ x ] = ( dx, dy )

    sinks = [ [ None ] * sx for x in xrange( sy ) ]
    letters = "abcdefghijklmnopqrstuvwxyz"
    i = 0
    for y in xrange( sy ) :
        for x in xrange( sx ) :
            xx, yy = x, y
            while sheds[ yy ][ xx ] != None :
                ( dx, dy ) = sheds[ yy ][ xx ]
                xx += dx
                yy += dy
            if sinks[ yy ][ xx ] == None :
                sinks[ yy ][ xx ] = letters[ i ]
                i += 1
            sinks[ y ][ x ] = sinks[ yy ][ xx ]
    return sinks

def solve( in_name, out_name ) :
    f_in = open( in_name, "r" )
    lines = f_in.readlines()
    f_in.close()

    f_out = open( out_name, "w" )
    N = int( lines[ 0 ].strip() )

    l = 1
    for i in xrange( N ) :
        ( H, W ) = [ int( x ) for x in lines[ l ].strip().split( " " ) ]
        l += 1

        field = []
        for j in xrange( H ) :
            field.append( [ int( x ) for x in lines[ l ].strip().split( " " ) ] )
            l += 1
        
        sinks = make_sheds( field )
        f_out.write( "Case #%d:\n" % ( i + 1 ) )
        for line in sinks :
            f_out.write( str( " " ).join( line ) + "\n" )
    f_out.close()


solve( "B-test.in", "B-test.out" )
solve( "B-small-attempt0.in", "B-small-attempt0.out" )
solve( "B-large.in", "B-large.out" )
