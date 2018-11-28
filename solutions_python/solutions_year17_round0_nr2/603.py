inf  = open( 'B-large.in', 'rb' )
outf = open( 'output.txt', 'wb' )

def runCase( caseId ):
    seq =  [ int(x) for x in str( int( inf.readline() ) )]
    top = [0] * len( seq )
    def check( i, val ):
        if i >= len( seq ):
            return True
        if seq[ i ] < val:
            return False
        if seq[ i ] > val:
            return True
        return check( i + 1, val )

    fill9 = False
    for i in xrange( len( seq ) ):
        if fill9:
            top[ i ] = 9
        elif check( i + 1, seq[i] ):
            top[ i ] = seq[ i ]
        else:
            top[ i ] = seq[ i ] - 1
            fill9 = True

    while top[0] == 0:
        top.pop( 0 )
    ans = ''.join( str(x) for x in top )
    outf.write('Case #%d: %s\n' % (caseId, ans))


T = int( inf.readline() )
for i in xrange( T ):
    runCase( i+ 1  )