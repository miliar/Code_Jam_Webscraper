inf  = open( 'B-large.in', 'rb' )
outf = open( 'output.txt', 'wb' )



def runCase( caseId ):
    C, J = [ int(x) for x in inf.readline().split(' ') ]
    ts = list()
    total = [0, 0]
    for i in xrange(J + C):
        a, b = map( int, inf.readline().split(' ') )
        ts.append( (a,b, i < C) )
        total[ i < C ] += b - a
    ts.sort()


    while True:
        n = len(ts)
        diffs = [ list(), list() ]
        for i in xrange( n ):
            d = ts[ ( i + 1 ) % n ][0] - ts[i][1]
            if d < 0:
                d += 1440
            if ts[ (i + 1 ) % n ][2] == ts[ i ][2]:
                diffs[ ts[i][2] ].append( (d, i) )
        changed = False
        for j in xrange(2):
            if len( diffs[ j ] ) == 0:
                continue
            x = diffs[j]
            x.sort()
            d, i = x[0]
            if total[ j ] + d <= 720:
                total[ j ] += d
                ts[i] = ( ts[i][0], ts[(i+1)%n][1], ts[i][2] )
                ts.pop( (i + 1 )%n )
                changed = True
                break
        if not changed:
            break
    c = 0
    n = len( ts )
    for i in xrange( n ):
        if ts[(i+1) % n][2] == ts[i][2]:
            c += 2
        else:
            c += 1

    outf.write('Case #%d: %d\n' % (caseId, c))


T = int( inf.readline() )
for i in xrange( T ):
    runCase( i+ 1  )