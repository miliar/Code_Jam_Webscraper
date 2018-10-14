import heapq
import sys

def solve(n, k):
    #Heap contains tuples (min(ls, rs), max(ls,rs), index, leftbound, rightbound)
    def get_optimal_position(left, right):
        span = right - left - 1
        return (-((span-1)/2), -(span/2), left + (span-1)/2 + 1, left, right)
    h = []
    heapq.heappush(h, get_optimal_position(0, n+1))
    low = 0
    high = 0
    for i in range(k):
        low, high, index, left, right = heapq.heappop(h)
        heapq.heappush(h, get_optimal_position(left, index))
        heapq.heappush(h, get_optimal_position(index, right))
    return -low, -high

def solve2(n, k):
    p = 1
    while p < n:
        p = p << 1
    p = p >> 1
    print n, p
    while p > 0:
        if k & p != 0:
            n = (n-1)/2
        else:
            n = n/2
        print n
        p = p >> 1
    return (n-1)/2, n/2

def solve3(n, k):
    def split(span_counts):
        out = {}
        for (span, count) in span_counts:
            for res in [(span-1)/2, span/2]:
                if res in out:
                    out[res] += count
                else:
                    out[res] = count
        return sorted(out.items(), reverse=True)
    span_counts = [(n, 1)]
    seen = 0
    while True:
        #print span_counts, seen
        for span, count in span_counts:
            seen += count
            if seen >= k:
                return (span-1)/2, span/2
        span_counts = split(span_counts)


lines = sys.stdin.readlines()
for i, l in enumerate(lines[1:]):
    n, k = map(int, l.strip().split(' '))
    lo, hi = solve3(n,k)
    print "Case #%d: %d %d" % (i+1, hi, lo)
