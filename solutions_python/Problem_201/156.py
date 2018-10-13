import heapq

t = int(raw_input())

for i in xrange(1, t + 1):
    n, k = [int(c) for c in raw_input().split(" ")]
    h = []
    heapq.heappush(h, -n)
    l, r = -1, -1
    for j in xrange(0, k):
        a = -heapq.heappop(h) - 1
        b, c = a / 2, a % 2
        l, r = b, b + c
        heapq.heappush(h, -r)
        heapq.heappush(h, -l)
    print "Case #{}: {} {}".format(i, r, l)
