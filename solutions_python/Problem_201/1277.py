from heapq import *

T = input()
for test in xrange(T):
    n, K = map(int, raw_input().split())
    h = []
    heappush(h, -n)
    l = r = None
    for i in xrange(K):
        x = -heappop(h)
        l = x / 2
        r = (x - 1) / 2
        heappush(h, -l)
        heappush(h, -r)
    print 'Case #%d: %d %d' % (test + 1, l, r)
