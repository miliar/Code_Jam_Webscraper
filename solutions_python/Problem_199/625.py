#!/usr/bin/python

import sys

def brute( S, K ):
    flips = 0
    for i in xrange( 0, len( S) ):
#        print ''.join(S)
#        print i, i+K, len(S)
        if S[i] != '+':
            if i+K > len(S):
                return 'IMPOSSIBLE'
            for j in xrange( 0, K ):
                if S[i+j] == '+':
                    S[i+j] = '-'
                else:
                    S[i+j] = '+'
            flips = flips + 1
    return flips

data = file(sys.argv[1]).read().splitlines()

NUMCASE = int(data.pop(0))

for CASE in xrange( 1, NUMCASE + 1 ):
    print 'Case #%d:' % ( CASE, ),
    (S, K) = data.pop(0).split()
    S = list(S)
    K = int(K)
    print brute( S, K )

        
