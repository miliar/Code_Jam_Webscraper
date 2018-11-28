# Python candir
from heapq import heappush, heappop
import sys

def solve(n, k):
    d = {}
    h = []
    heappush(h, -n)
    d[n] = 1
    while k != 0:
        x = -heappop(h)
        c = d[x]
        if x % 2 == 0:
            y1 = (x - 1) // 2 + 1
            y2 = (x - 1) // 2 
        else:
            y1 = y2 = (x - 1) // 2
        if k <= c:
            return (y1, y2)
        k -= c
        if y1 in d:
            d[y1] += c
        else:
            d[y1] = c
            heappush(h, -y1)
        if y2 in d:
            d[y2] += c
        else:
            d[y2] = c
            heappush(h, -y2)

with open(sys.argv[1], 'r') as fin:
    with open(sys.argv[2], 'w') as fout:
        t = int(fin.readline())
        for i in range(1, t+1):
            s = fin.readline().split()
            n = int(s[0])
            k = int(s[1])
            res = solve(n, k)
            print("Case #{}: {} {}".format(i, res[0], res[1]), file=fout)

