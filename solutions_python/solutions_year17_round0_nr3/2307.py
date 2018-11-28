import heapq
import sys

def solve(n, k):
    l = [-n]
    heapq.heapify(l)
    for i in range(k):
        e = heapq.heappop(l)
        a, b = -e//2, (-e-1)//2
        if i == k-1:
            return a, b
        else:
            heapq.heappush(l, -a)
            heapq.heappush(l, -b)

with open(sys.argv[1]) as fh:
    T = int(next(fh))
    for i, line in enumerate(fh):
        n, k = line.split()
        n, k = int(n), int(k)
        print("Case #{}: {} {}".format(i+1, *solve(n, k)))
