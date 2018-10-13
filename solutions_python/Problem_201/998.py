import heapq

t = input()
for cas in xrange(t):
    n, k = map(int, raw_input().split())
    h = []
    heapq.heappush(h, (-n, 0, n+1))
    for i in xrange(k):
        size, l, r = heapq.heappop(h)
        size = -size
        flag = (size % 2 == 1)
        size /= 2

        if flag:
            heapq.heappush(h, (-size, l, l+size+1))
            heapq.heappush(h, (-size, l+size+1, r))
        else:
            heapq.heappush(h, (1-size, l, l+size))
            heapq.heappush(h, (-size, l+size, r))

        if i == k-1:
            print 'Case #{0}: {1} {2}'.format(cas+1, size, size if flag else size-1)
