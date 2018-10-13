


def writeFile( results ):
    outFile = "A.txt"
    try:
        f = open( outFile, "w" )
        try:
            for i, result in enumerate( results ):
                # space between
                f.write( "Case #{0}: {1}\n".format( i+1, result ) )
        finally:
            f.close()
    except IOError:
        pass

def readFile( infile ):
    lines = [line.strip() for line in open( infile )]
    return lines


def checkSquare( s ):
    n = False
    for i in s:
        if '.'in i: n = True
        elif not 'X' in i: return 'O won'
        elif not 'O' in i: return 'X won'
    if n: return 'Game has not completed'
    return 'Draw'

def parse( lines ):
    result = []
    T = int( lines[0] )
    for i in range( T ):
        s = []
        for j in range( 4 ):
            # hor line
            s.append( lines[i * 5 + j + 1] )
        # vert
        s.append( '{0}{1}{2}{3}'.format( s[0][0], s[1][0], s[2][0], s[3][0] ) )
        s.append( '{0}{1}{2}{3}'.format( s[0][1], s[1][1], s[2][1], s[3][1] ) )
        s.append( '{0}{1}{2}{3}'.format( s[0][2], s[1][2], s[2][2], s[3][2] ) )
        s.append( '{0}{1}{2}{3}'.format( s[0][3], s[1][3], s[2][3], s[3][3] ) )
        # diag
        s.append( '{0}{1}{2}{3}'.format( s[0][0], s[1][1], s[2][2], s[3][3] ) )
        s.append( '{0}{1}{2}{3}'.format( s[0][3], s[1][2], s[2][1], s[3][0] ) )
        result.append( checkSquare( s ) )
    return result


lines = readFile( 'A-large.in' )
results = parse( lines )
writeFile( results )

