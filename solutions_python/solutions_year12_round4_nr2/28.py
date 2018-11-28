# B
from sys import stdin, stderr
import random

def distok(a, b, r):
    x = a[0] - b[0]
    y = a[1] - b[1]
    return x*x + y*y >= r*r

T=int(stdin.readline())
for t in xrange(1, T+1):
    N,W,L=map(int, stdin.readline().split())
    R = map(int, stdin.readline().split())
    RS = [ (R[i], i) for i in xrange(N) ]
    RS.sort(key=lambda x: -x[0])
    
    pref=[(W,L), (W, 0), (0, L), (0,0)]
    
    pos = dict()
    ptr = 0
    while ptr < N:
        r = RS[ptr]
        ptr += 1

        for z in xrange(10000):
            if len(pref)>0:
                pt = pref.pop()
            else:
                pt = (random.randint(0, W), random.randint(0, L))
            
            print >>stderr, z, pt
            
            ok = True
            for i,p in pos.items():
                if not distok(p, pt, r[0] + R[ i ]):
                    ok = False
                    break
            if ok:    
                pos[ r[1] ] = pt
                break
        if r[1] not in pos:
            print >>stderr, 'Failed'
    
    print 'Case #%d:' % t,
    for i in xrange(N):
        print '%f %f' % (pos[i][0], pos[i][1]),
    print ''