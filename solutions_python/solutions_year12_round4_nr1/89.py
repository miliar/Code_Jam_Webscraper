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

best_for_d = {}
def can_win_from(vine, h, vines, D):
    global tried_ds
    max_d = vine[0] + h
    min_d = vine[0] - h
    if min_d <= D <= max_d:
        return True
    for i in xrange(len(vines)):
        if min_d <= vines[i][0] <= max_d:
            vine_h = min(vines[i][1], abs(vines[i][0]-vine[0]))
            if vine_h > best_for_d[vines[i][0]]:
                best_for_d[vines[i][0]] = vine_h
                if can_win_from(vines[i], vine_h, vines, D): return True
    return False

def do_test(vines, D):
    global best_for_d
    best_for_d = {}
    for vine in vines:
        best_for_d[vine[0]] = 0
    if can_win_from(vines[0], vines[0][0], vines, D):
        return "YES"
    else:
        return "NO"

            
T=int(raw_input())
for i in xrange(T):
    N = int(raw_input())
    vines = [map(int, raw_input().split()) for n in xrange(N)]
    D = int(raw_input())
    print 'Case #%d:' % (i+1), do_test(vines, D)
    print >>sys.stderr, 'test', i+1
