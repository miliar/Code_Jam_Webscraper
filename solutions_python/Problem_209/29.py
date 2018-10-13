import math

inf  = open( 'A-large.in', 'rb' )
outf = open( 'output.txt', 'wb' )

def runCase( caseId ):
    N, K = inf.readline().split( ' ' )
    N = int( N )
    K = int( K )

    pancakes = list()
    for i in xrange( N ):
        r, h = inf.readline().split( ' ' )
        r = int(r)
        h = int(h)
        surf = math.pi * 2 * r * h
        pancakes.append( (h, r) )
    pancakes.sort( key = lambda x: x[0] * x[1] )
    pancakes = pancakes[::-1]
    #print pancakes
    ans = 0
    for i in xrange( N ):
        maxR = pancakes[i][1]
        surf = math.pi * maxR**2 + 2 * math.pi * maxR * pancakes[i][0]
        total = 1
        for j in xrange( N ):
            if total == K:
                break
            if i == j:
                continue
            if pancakes[j][1] <= maxR:
                total += 1
                surf += 2 * math.pi * pancakes[j][1] * pancakes[j][0]
        if total < K:
            continue
        if ans < surf:
            ans = surf

    outf.write('Case #%d: %.10f\n' % (caseId, ans))


T = int( inf.readline() )
for i in xrange( T ):
    runCase( i+ 1  )