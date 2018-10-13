"""C
   Google CodeJam 2009
"""

from datetime import datetime
import bisect

#from itertools in python 2.6
#http://docs.python.org/library/itertools.html
def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

        
def routine(P, Q, qs):
    best = 999999999
#>>> d[bisect.bisect(d,(12,12))-1]
#(7, 11)
#>>> d[bisect.bisect(d,(7,7))-1]
#(3, 6)    
    for attempt in permutations(qs):
        ps = []
        bisect.insort(ps, (1,P))
        coins = 0
        for q in attempt:
            i = bisect.bisect(ps, (q+1,q+1))
            t = ps[i-1]
            #print "Splitting", i, t, "with", q
            coins += (t[1] - t[0])
            if coins == best:                
                break
            del(ps[i-1])
            if t[0] != q:
                bisect.insort(ps, (t[0], q-1))
            if t[1] != q:
                bisect.insort(ps, (q+1, t[1]))
            
            #print ps
            
        if coins < best:
            best = coins
    
    return best

if __name__ == '__main__':
    filename = "C-small-attempt0"
    f = open(filename + ".in")
    fo = open(filename + ".out", "w")

    print datetime.now()

    c = int(f.readline())
    print c, "cases"
    for case in xrange(c):
        P, Q = [int(x) for x in f.readline().split()]
        qs = [int(x) for x in f.readline().split()]

        print P, Q
        print qs

        print
        print >>fo, "Case #%d: %s" % (case+1, routine(P, Q, qs))

    fo.close()
    f.close()
    print datetime.now()
