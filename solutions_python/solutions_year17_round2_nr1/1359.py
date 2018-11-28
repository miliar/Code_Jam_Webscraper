#!/usr/bin/python

import sys

def brute2( D, N, P, V ):
    t = 0.0
    while P[0] < D:
        # find next collision
        colt = 99999999.0
        for i in xrange(0,N-1):
            if V[i] < V[i+1]:
                break
            if V[i] > V[+1]:
                cc = (P[i+1] - P[i]) / (V[i] - V[i+1])
                colt = min(colt,cc)

        if colt == 99999999.0:
            # calc rem time
            t = t + (D - P[0]) / V[0]
            break
        else:
            # adjust everyone
            for i in xrange(0,N-1):
                P[i] = P[i] + (V[i] * colt)
            # adjust velocity
            for i in xrange(0,N-1):
                if P[i] >= P[i+1] and V[i] > V[i+1]:
                    V[i] = V[i+1]
            t = t + colt
            
    return '%0.6f' % ( D / t )
        
def brute( D, N, P, V ):
    t = 0.0
    for i in xrange(0,N):
        tt = (D-P[i]) / V[i]
        t = max(t,tt)

    return '%0.6f' % ( D / t )
        

data = file(sys.argv[1]).read().splitlines()

NUMCASE = int(data.pop(0))

for CASE in xrange( 1, NUMCASE + 1 ):
    print 'Case #%d:' % ( CASE, ),
    (D, N) = [int(x) for x in data.pop(0).split()]
    D = float(D)
    P = []
    V = []
    PV = []
    for i in xrange(0,N):
        (p, v) = [float(x) for x in data.pop(0).split()]
        PV.append((p,v))

    PV.sort()
    for p,v in PV:
        P.append(p)
        V.append(v)
    print brute( D, N, P, V )

        
