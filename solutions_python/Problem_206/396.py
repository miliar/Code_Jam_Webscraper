inf  = open( 'A-large.in', 'rb' )
outf = open( 'output.txt', 'wb' )

def runCase( caseId ):
    D, N = inf.readline().split( ' ' )
    D = int( D )
    N = int( N )
    ans = 0
    for i in xrange( N ):
        k, s = inf.readline().split( ' ' )
        k = int( k )
        s = int( s )
        ans = max( ans, float( D - k ) / s )
    ans = float( D ) / ans
    outf.write('Case #%d: %.6f\n' % (caseId, ans))


T = int( inf.readline() )
for i in xrange( T ):
    runCase( i+ 1  )