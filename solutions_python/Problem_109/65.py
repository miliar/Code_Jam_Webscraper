#2213
#
#? min

import sys
import copy
import math

EP=1E-7
INF=1E17

def apx_equal(x,y):
    return abs(x-y)<EP

def dist(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def trace_call(fn):
    def new_fn(*args,**kwargs):
        ret = fn(*args,**kwargs)
        print >>sys.stderr, fn.__name__, '(',
        if args:
            print >>sys.stderr, ','.join(map(str,args)),
            if kwargs:
                print >>sys.stderr,',',
        if kwargs:
            print >>sys.stderr, ','.join(['%s=%s'%(map(str,k,v)) for k,v in kwargs.iteritems()]),
        print >>sys.stderr,')', '=', ret
        return ret
    new_fn.__name__ = fn.__name__
    return new_fn

def memo(fn):
    m = {}
    def new_fn(*args,**kwargs):
        h = hex(hash(str(args)+'/'+str(kwargs)))
        if h not in m:
            m[h] = fn(*args,**kwargs)
        return m[h]
    new_fn.__name__= fn.__name__
    return new_fn

class ProblemsError(Exception): pass

def do_test(W,L,R):
    #R.sort(reverse=True)
    l_delta = L / 275.  #try up to ~75k places each
    w_delta = W / 275.
    placed = []
    for r in R:
        w=0
        found = False
        while w < W:
            l=0
            while l < L:
                bad = False
                for p in placed:
                    if dist(p[0],p[1],w,l) <= p[2]+r:
                        bad = True
                        break
                if not bad:
                    print >>sys.stderr, 'placed', r, 'at', w, l
                    placed.append((w,l,r))
                    found = True
                    break
                l += l_delta
            if found:
                break
            w += w_delta
        if not found:
            raise ProblemsError
    end_placed=[(p[0],p[1]) for p in placed]
    return ' '.join(['%.6f %.6f' % (p[0],p[1]) for p in end_placed])

            
T=int(raw_input())
for i in xrange(T):
    N,W,L = map(int, raw_input().split())
    R = map(int, raw_input().split())
    print 'Case #%d:' % (i+1), do_test(W,L,R)
    print >>sys.stderr, 'test', i+1
