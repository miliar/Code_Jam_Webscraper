import sys
import heapq


def go(n, k):
    h = [-n]
    for i in xrange(k):
        max_gap = -heapq.heappop(h)
        assert max_gap > 0
        if max_gap % 2 == 1:
            heapq.heappush(h, -((max_gap - 1) / 2))
            heapq.heappush(h, -((max_gap - 1) / 2))
            a = b = (max_gap - 1) / 2
        else:
            heapq.heappush(h, -(max_gap / 2))
            heapq.heappush(h, -((max_gap / 2) - 1))
            a = (max_gap / 2)
            b = max_gap / 2 - 1
    return a, b


def solve(n, k):
    return go(n, k)


T = int(sys.stdin.readline())
for i in xrange(T):
    n, k = map(int, sys.stdin.readline().split())
    a, b = solve(n, k)
    print 'Case #%d: %d %d' % (i+1, a, b)
