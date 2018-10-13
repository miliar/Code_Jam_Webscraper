import psyco
psyco.full()
filename = 'c'
MAXN = 25
cache = {}
def comb( m, n ):
    key = ( m, n )
    if key in cache:
        return cache[key]
    s = 1
    for i in xrange( 1, m + 1 ):
        s = ( s * ( n - i + 1 ) / i ) % 100003
    cache[key] = s
    return s

fin = open( filename + '.in' )
fout = open( filename + '.out', 'w' )
testcases = int( fin.readline() ) + 1
f = []
for i in xrange( MAXN + 1 ):
    f.append( [0] * MAXN )
for n in xrange( 2, MAXN + 1 ):
    f[n][1] = 1
    for k in xrange( 2, n ):
        for t in xrange( 1, k ):
            if k - t <= n - k:
                f[n][k] += f[k][t] * comb( k - t - 1, n - k - 1 )
for case in xrange( 1, testcases ):
    n = int( fin.readline() )
    fout.write( 'Case #%d: %d\n' % ( case, sum( f[n] ) % 100003 ) )
fin.close()
fout.close()
