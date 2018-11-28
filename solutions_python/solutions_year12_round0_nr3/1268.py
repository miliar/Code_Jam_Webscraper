def solve( lower , higher ):
    digs = len( str( lower ) )
    den = 1
    for x in range( digs - 1 ) :
        den *= 10

    pairs = 0
    cc = []
    for x in range( lower , higher + 1 ) :
        x0 = x
        goods = 0
        items = 1
        if ( ( x0 <= higher ) and ( x0 >= lower ) ) :
            goods += 1
        else :
            continue
        for k in range( digs ) :
            x = ( x % den ) * 10 + x / den
            if ( ( x / den != 0 ) and ( x0 != x ) ) :
                items += 1
                if ( ( lower <= x ) and ( higher >= x ) ) :
                    goods += 1
                    if ( x < x0 ) :
                        cc.append( ( x0 , x ) )


        pairs += ( goods - 1 ) / 2.0
    return len( cc )

def main():
    fIn = open( "C:\\gjam\\cycles\\in.txt" )
    fOut = open( "C:\\gjam\\cycles\\out.txt" , 'w' )
    tasksCount = int( fIn.readline() )
    for task in range( 1 , tasksCount + 1 ) :
        lower , higher = [ int( x ) for x in fIn.readline().split() ]
        fOut.write( 'Case #' + str( task ) + ': ' + str( solve( lower , higher ) ) + '\n' )



if __name__ == '__main__':
    main()
