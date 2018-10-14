from collections import defaultdict

inf  = open( 'C-large.in', 'rb' )
outf = open( 'output.txt', 'wb' )

def runCase( caseId ):
    n, k = inf.readline().split(' ')
    n = int( n )
    k = int( k ) - 1

    intervals = { n : 1 }

    total = 1

    while ( total < k ):
        new_intervals = defaultdict( int )
        total = 0
        for s, no in intervals.iteritems():
            new_intervals[ (s-1)/2 ] += no
            new_intervals[ s - 1 - (s-1)/2 ] += no
            k -= no
            total += 2 * no
        intervals = new_intervals

    y = 0
    z = 0
    def f( s, y, z ):
        minS = (s-1)/2
        maxS = s - 1 - (s-1)/2
        if y < minS:
            y = minS
            z = maxS
        elif z == minS:
            z = max( maxS, z )
        return y, z

    print intervals

    for s in sorted( intervals.keys() )[::-1]:
        if s == 0:
            continue
        if intervals[ s ] > k:
            y,z = f( s, y,z  )
        else:
            y,z = f( (s-1)/2, y,z )
            y,z= f( s - 1 - (s-1)/2, y,z )
            k -= intervals[s]

    outf.write('Case #%d: %d %d\n' % (caseId, z, y ))


T = int( inf.readline() )
for i in xrange( T ):
    runCase( i+ 1  )