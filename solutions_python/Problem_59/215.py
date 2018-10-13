#import psyco
#psyco.full()

import sys, copy


def calc2(ndirs, mdirs):
    nndirs = set()
    for nd in ndirs:
        pd = ''
        for d in nd.split('/'):
            if d in ('', '/'):
                continue
            nndirs.add(pd)
            pd += '/' + d
        nndirs.add(pd)
    #print "SSSSSSSS", ndirs, nndirs, mdirs
    ndirs = nndirs
    
    c = 0
    for m in mdirs:
        if m in ndirs:
            continue
        pd = ''
        for d in m.split('/'):
            if d in ('', '/'):
                continue
            pd += '/' + d
            if not pd in ndirs:
                c += 1
                ndirs.add(pd)
    return c


def calc(ndirs, mdirs, c=None):
    if c==None:
        nndirs = set()
        for nd in ndirs:
            pd = '/'
            for d in nd.split('/'):
                nndirs.add(pd)
                pd += '/' + d
            nndirs.add(pd)
        print "SSSSSSSS", ndirs, nndirs, mdirs
        ndirs = nndirs
    if c==None:
        c=0
    
    for m in mdirs:
        while not m in ndirs and not (m in ('','/')):
            pm = m[0:m.rfind('/')]
            ndirs.add(pm)
            print 'QQQQQ', ndirs, pm, m
            c = 1 + calc(ndirs, set((pm,)), c)
    return c



def inGen():
    for line in open(sys.argv[1], 'r'):
        yield line.strip('\n')

ig = inGen()
ig.next()
cn = 1
for line in ig:
    N,M = [int(s) for s in line.split(' ')]
    ndirs = set()
    mdirs = set()
    for nd in xrange(N):
        ndirs.add(ig.next())
    for md in xrange(M):
        mdirs.add(ig.next())
    v = calc2(ndirs,mdirs)
    print "Case #%d: %d" % (cn,v)
    cn += 1
