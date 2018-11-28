import sys
import heapq

fp = open(sys.argv[1])
N = int(fp.readline().strip())

def foo(line):
    N, K = line.split(" ")
    N = int(N)
    K = int(K)
    if (N == K):
        return "0 0"
    if (N + 2) * 2 / 3 < K:
        return "0 0"
    h = [0]
    heapq.heapify(h)
    for k in range(K):
        n = heapq.heappop(h)
        n = N - n
        l = n / 2
        r = n - l - 1
        if k == K - 1:
            # last one
            return "%d %d" % (max(l, r), min(l, r))
        if l > 0:
            heapq.heappush(h, N - l)
        if r > 0:
            heapq.heappush(h, N - r)

for case in range(N):
    print 'Case #%d: %s' % (case + 1, foo(fp.readline().strip()))
fp.close()

