
def isPalin( num ):
    return str( num ) == str( num )[::-1]


def writeFile( results ):
    outFile = "C.txt"
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


fs = []
for i in range( 19999999 ):
    s = i * i
    if isPalin( s ) and isPalin( i ):
        fs.append( s )


def check( l, h  ):
    count = 0;
    for i in fs:
        if i >= l and i <= h:
            count += 1
    return str( count )

def parse( lines ):
    result = []
    T = int( lines[0] )
    for i in range( T ):
        n = lines[i + 1].split()
        result.append( check( long( n[0] ), long( n[1] ) ) )
    return result


lines = readFile( 'C-large-1.in' )
results = parse( lines )
writeFile( results )

print 'done'