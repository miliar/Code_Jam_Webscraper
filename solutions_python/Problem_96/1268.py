from math import ceil

def solve( ss , th , sums ) :
    p1 = [ ceil( s / 3.0 ) for s in sums ]
    prets = 0
    above = 0
    for i in range( len( sums ) ) :
        resid = sums[ i ] % 3
        if ( p1[ i ] == th-1 ) :
            if ( resid == 0 ) :
                if ( ( p1[ i ] != 0 ) and ( p1[ i ] != 10 ) ) :
                    prets += 1
            if ( resid == 2 ) :
                if ( p1[ i ] != 10 ) :
                    prets += 1

        if ( p1[ i ] >= th ) :
            above += 1
    return above + min( prets , ss )


def main():
    fIn = open( "C:\\gjam\\googlers\\in.txt" )
    fOut = open( "C:\\gjam\\googlers\\out.txt" , 'w' )
    tasksCount = int( fIn.readline() )
    for task in range( 1 , tasksCount + 1 ) :
        nums = [ int( x ) for x in fIn.readline().split() ]
        fOut.write( 'Case #' + str( task ) + ': ' + str( solve( nums[ 1 ] , nums[ 2 ] , nums[ 3 : ] ) ) + '\n' )


if __name__ == '__main__':
    main()