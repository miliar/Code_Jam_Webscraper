import heapq
from collections import Counter

def dec(heap, count, m):
    count[m] -= 1
    if count[m] == 0:
        heapq.heappop(heap)

def inc(heap, count, a, c):
    if count[a] > 0:
        count[a] += c
    else:
        heapq.heappush(heap, -a)
        count[a] = c

for t in xrange(input()):
    n, k = map(int, raw_input().split())
    count = Counter()
    heap = []
    heapq.heappush(heap, -n)
    count[n] = 1
    ans = (0, 0)
    pool = k
    while pool > 0:
        m = -heapq.heappop(heap)
        c = count[m]
        m -= 1
        a = m / 2
        b = m - a
        ans = (b, a)
        inc(heap, count, a, c)
        inc(heap, count, b, c)
        pool -= c
    print "Case #%d: %d %d" % (t + 1, ans[0], ans[1])

