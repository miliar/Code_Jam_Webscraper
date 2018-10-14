import heapq
import math
import sys

N = 1000
K = 1000


def gen(n):
    h = []
    heapq.heappush(h, -n)
    while h:
        n = -heapq.heappop(h)
        middle = math.floor((n - 1) / 2.0)
        mx, mn = n - middle - 1, middle
        if mx > 0:
            heapq.heappush(h, -mx)
        if mn > 0:
            heapq.heappush(h, -mn)
        yield middle, mx, mn


def result(N, K):
    g = gen(N)
    for _ in range(K):
        _, mx, mn = g.next()
    return mx, mn


# g = gen(10)
# for _ in range(10):
#     print g.next()

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    for i in range(N):
        N, K = map(int, sys.stdin.readline().strip().split(" "))
        mx, my = result(N, K)
        print "Case #%d: %d %d" % (i + 1, mx, my)
