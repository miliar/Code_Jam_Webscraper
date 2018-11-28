#import psyco
#psyco.full()

import sys, copy, decimal


def calc(N,K,B,T,xs,vs):
    s = 0
    c = 0
    #print "QQQ", N, K, int(B), T, [int(n) for n in xs], [int(n) for n in vs], [float((B-xs[ci])/vs[ci]) for ci in xrange(N)]
    for ci in reversed(xrange(N)):
        if c == K:
            break 
        cd,cv = B-xs[ci], vs[ci]
        ct = cd / cv
        if ct > T:
            continue
        c += 1
        for bci in xrange(ci+1,N):
            bcd, bcv = B-xs[bci], vs[bci]
            bct = bcd / bcv
            if bct > ct and bct > T:
                s += 1
                #print "KKKKKK", bct
                #print "KKKKKK", ct
                #print
            #diff = (bct-ct).copy_abs()
            #if diff < 1:
            #    print 'RSRS', cd,cv,ct, '::::', bcd,bcv,bct 
    if c < K:
        return "IMPOSSIBLE"
    else:
        return s


def inGen():
    for line in open(sys.argv[1], 'r'):
        yield line.strip('\n')

ig = inGen()
ig.next()
cn = 1
for line in ig:
    N,K,B,T = [int(s) for s in line.split(' ')]
    B = decimal.Decimal(str(B))
    T = decimal.Decimal(str(T))
    xs = [decimal.Decimal(s) for s in ig.next().split(' ')]
    vs = [decimal.Decimal(s) for s in ig.next().split(' ')]
    v = calc(N,K,B,T,xs,vs)
    print "Case #%d: %s" % (cn,str(v))
    cn += 1
