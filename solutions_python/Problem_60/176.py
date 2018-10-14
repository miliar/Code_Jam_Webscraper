#!/usr/bin/env python
import sys

class coisa(object):
    def __init__(self, x, v, t, b):
        self.x = x
        self.v = v
        self.can_arrive = (x + v*t) >= b
        
def time_to_switch(chickens, cidx, i):
    t = 0
    return t

def go():
    n, k, b, t = map(int, sys.stdin.readline().split())
    x = map(int, sys.stdin.readline().split())
    v = map(int, sys.stdin.readline().split())
    chickens = [coisa(xp, vp, t, b) for (xp, vp) in zip(x, v)]
    can_indexes = [i for i in xrange(len(chickens)) if chickens[i].can_arrive]
    if len(can_indexes) < k:
        return None
    total_swaps = 0
    
    for blaargh in xrange(k):
        can_indexes = reversed([i for i in xrange(len(chickens)) if chickens[i].can_arrive])
        #print >> sys.stderr, can_indexes
        cidx = n-1-blaargh
        if chickens[cidx].can_arrive:
            continue
        else:
            switched = False
            for i in can_indexes:
                if i >= cidx:
                    continue
                if time_to_switch(chickens, cidx, i) <= t:
                    total_swaps += cidx - i
                    val = chickens[i]
                    for j in xrange(i,cidx):
                        chickens[j] = chickens[j+1]
                    chickens[cidx] = val
                    switched = True
                    #print >>sys.stderr, 'switched %d with %d at cost %d' % (i, cidx, cidx-i)
                    break
            if not switched:
                return None

    return total_swaps

if __name__ == '__main__':
    C = int(sys.stdin.readline())
    for c in xrange(1, C+1):
        x = go()
        print 'Case #%d: %s' % (c, str(x) if x is not None else 'IMPOSSIBLE')
