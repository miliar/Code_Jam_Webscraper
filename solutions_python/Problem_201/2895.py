import heapq
import sys

t = int(raw_input())

for c in xrange(1,t+1):
    n, k = map(int,raw_input().split())
    h = []
    heapq.heappush(h, n*-1)
    for i in xrange(k):
        target = heapq.heappop(h) * -1 - 1
        mod = target % 2
        small = target // 2
        large = small + mod
        heapq.heappush(h, small * -1)
        heapq.heappush(h, large * -1)
    print "Case #"+str(c)+": "+str(large)+" "+str(small)
