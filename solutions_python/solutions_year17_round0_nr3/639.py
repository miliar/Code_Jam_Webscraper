#!/usr/bin/python

import sys, collections

def brute( N, K ):
    E = collections.defaultdict(int)
    E[N] = 1
    while K:
        m = max(E.keys())
        if K > E[m]:
            if m % 2:
                # odd, split into two even buckets
                s = (m - 1) / 2
                E[s] = E[s] + ( E[m] * 2 )
            else:
                s = (m - 1 ) / 2
                E[s] = E[s] + E[m]
                E[s+1] = E[s+1] + E[m]
            K = K - E[m]
            del E[m]
        else:
            if m % 2:
                # odd. Ls and Rs are the same:
                return '%d %d' % ( m / 2, m / 2 )
            else:
                return '%d %d' % ( m / 2, (m / 2) - 1 )
                

data = file(sys.argv[1]).read().splitlines()

NUMCASE = int(data.pop(0))

for CASE in xrange( 1, NUMCASE + 1 ):
    print 'Case #%d:' % ( CASE, ),
    (N, K) = [int(x) for x in data.pop(0).split()]
    print brute( N, K )

        
