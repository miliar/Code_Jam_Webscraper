import math
import sys
import heapq

data = sys.stdin.readlines()
t = int(data[0])
for i in range(t):
    print "Case #%d:" % (i+1),

    d = data[i+1].split()

    n = int(d[0])
    k = int(d[1])

    h = [-n]
    
    for j in range(k):
        m = -heapq.heappop(h)
        m1 = int(math.ceil((m-1)/2.0))
        m2 = int(math.floor((m-1)/2.0))

        if m1 > 0:
            heapq.heappush(h, -m1)
        if m2 > 0:
            heapq.heappush(h, -m2)
    
    print "%d %d" % (m1, m2)
