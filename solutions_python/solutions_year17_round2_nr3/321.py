from collections import defaultdict

inf  = open( 'C-small-attempt0.in', 'rb' )
outf = open( 'output.txt', 'wb' )

def runCase( caseId ):
    N, Q = inf.readline().split(' ')
    N = int(N)
    Q = int(Q)

    E = list()
    S = list()
    dist = list()

    for i in xrange( N ):
        e, s = inf.readline().split(' ')
        E.append( int(e) )
        S.append( int(s) )

    for i in xrange( N ):
        if i < N - 1:
            dist.append( int ( inf.readline().split( ' ' )[ i + 1] ) )
        else:
            inf.readline()
    for _ in xrange( Q ):
        inf.readline()

    T = [ -1 for _ in xrange(N) ]
    T[ 0 ] = 0
    for i in xrange( N - 1 ):
        total_dist = 0
        for j in xrange( i + 1, N ):
            total_dist += dist[j - 1]
            if total_dist <= E[i]:
                time = T[ i ] + float( total_dist ) / S[i]
                if T[j] == -1 or T[j] > time:
                    T[j] = time

    outf.write('Case #%d: %.6f\n' % (caseId, T[N-1] ))


T = int( inf.readline() )
for i in xrange( T ):
    runCase( i+ 1  )