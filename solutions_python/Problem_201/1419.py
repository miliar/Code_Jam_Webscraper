import sys
import heapq
input = open(sys.argv[1])


def solve(v):
    v = v.split()
    n, k = int(v[0]), int(v[1])
    h = []
    heapq.heappush(h, -n)
    for _ in range(k - 1):
        x = -heapq.heappop(h)
        if x % 2:
            heapq.heappush(h, -(x // 2))
            heapq.heappush(h, -(x // 2))
        else:
            heapq.heappush(h, -(x // 2))
            heapq.heappush(h, -(x // 2 - 1))

    x = -(heapq.heappop(h))
    # print (v, x, x // 2, x // 2 - (x + 1) % 2)
    return x // 2, x // 2 - (x + 1) % 2


for i, v in enumerate([x for x in input.readlines()][1:]):
    print ("Case #%d: %d %d" % (i + 1, *solve(v)))
