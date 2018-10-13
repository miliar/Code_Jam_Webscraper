import sys
import heapq

lines = open(sys.argv[1], "rb").read().splitlines()
res = ""

for t, line in enumerate(lines[1:]):
    n, k = map(int, line.split(' '))
    h = [-n]
    cur = ()
    for i in xrange(k):
    	x = -heapq.heappop(h)
    	cur = (x / 2, x / 2 - 1 + x % 2)
    	heapq.heappush(h, -cur[0])
    	heapq.heappush(h, -cur[1])
    res += "Case #%d: %d %d\n" % (t + 1, cur[0], cur[1])

open(sys.argv[2], "wb").write(res)
