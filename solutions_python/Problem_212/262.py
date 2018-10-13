import math

from collections import defaultdict

inf  = open( 'A-small-attempt0.in', 'rb' )
outf = open( 'output.txt', 'wb' )

def runCase( caseId ):
    N, P = map( int, inf.readline().strip().split( ' ' ) )

    gs = map( int, inf.readline().strip().split(' ') )
    gs = [ x % P for x in gs ]
    np = defaultdict( int )
    for g in gs:
        np[ g ] += 1
    if P == 1:
        ans = len( gs )
    elif P == 2:
        ans = np[ 0 ] + ( np[ 1 ] + 1 ) / 2
    elif P == 3:
        ans = np[ 0 ]
        addf = min( np[ 1 ], np[ 2 ] )
        ans += addf
        np[ 1 ] -= addf
        np[ 2 ] -= addf
        ans += ( np[ 1 ] + 2 ) / 3 + ( np[2] + 2 ) / 3
    elif P == 4:
        ans = np[ 0 ]
        addf = min( np[1], np[3] )
        ans += addf
        np[ 1 ] -= addf
        np[ 3 ] -= addf
        ans += np[2] / 2
        np[2] = np[2] % 2

        addf = min( np[1] / 2, np[2] )
        ans += addf
        np[1] -= addf * 2
        np[2] -= addf
        addf = min( np[3] / 2, np[2] )
        np[3] -= addf*2
        np[2] -= addf

        ans += np[1] / 4
        np[1] = np[1] % 4
        ans += np[3] / 4
        np[3] = np[3] % 4

        if np[1]+np[2]+np[3] > 0:
            ans += 1

    outf.write('Case #%d: %d\n' % (caseId, ans))


T = int( inf.readline() )
for i in xrange( T ):
    runCase( i+ 1  )