from collections import defaultdict
def f():
    tc, = map(int, raw_input().split())
    for _tc in xrange(tc):
        n, k = map(int, raw_input().split())
        d = defaultdict(int)
        d[n] = 1
        res = None
        while k > 0:
            n = max(d)
            v = d[n]
            if n&1: 
                res = (n//2, n//2)
            else:
                res = (n//2, n//2-1)
            #print k, n, v, res
            d[res[0]] += v
            d[res[1]] += v
            del d[n]
            k -= v

        print 'Case #%d: %d %d' % (_tc+1, max(res), min(res))
f()


