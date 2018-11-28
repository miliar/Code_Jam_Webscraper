def writeFile( results ):
    outFile = "B.txt"
    try:
        f = open( outFile, "w" )
        try:
            for i, result in enumerate( results ):
                # space between
                f.write( "Case #{0}: {1}\n".format( i + 1, result ) )
        finally:
            f.close()
    except IOError:
        pass

def readFile( infile ):
    lines = [line.strip() for line in open( infile )]
    return lines

def checkSquare( r, c, s ):
    for i in range( c ):
        
        cmin = min( s[r + i] )
        cmax = max( s[r + i] )
        
        if cmin != cmax:
            for j in range( r ):
                if s[r + i][j] == cmin:
                    rmax = max( s[j] )
                    if rmax > cmin: return 'NO'
    return 'YES'

def parse( lines ):
    result = []
    T = int( lines[0] )
    L = 1
    for _i in range( T ):
        rc = lines[L].split()
        n = int( rc[0] )
        m = int( rc[1] )
        s = []
        # rows
        for j in range( n ):
            s.append( [] )
            row = lines[L + 1 + j].split()
            for k in range( m ):
                s[j].append( int( row[k] ) )
        # cols
        for k in range( m ):
            s.append( [] )
            for j in range( n ):
                s[n + k].append( s[j][k] )

        result.append( checkSquare( n, m, s ) )
        L = L + n + 1
    return result


lines = readFile( 'B-small-attempt2.in' )
results = parse( lines )
writeFile( results )


