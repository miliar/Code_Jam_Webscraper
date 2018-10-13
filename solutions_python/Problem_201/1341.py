import heapq
from math import floor, ceil
t = int(raw_input())
ans = []
for h in range(t):
    n, k = map(int, raw_input().split())
    p = [-n]
    heapq.heapify(p)
    for i in range(k-1):
        #print i+1, p
        x = -heapq.heappop(p)
        if x == 1:
            break
        y = int(floor((x-1)/2.0))
        z = int(ceil((x-1)/2.0))
        heapq.heappush(p,-y)
        heapq.heappush(p,-z)
        #print p
    x = -heapq.heappop(p)
    y = int(floor(x/2.0))
    z = int(floor((x-1)/2.0))
    ans.append((y,z))
for h in range(t):
    print 'Case #'+str(h+1)+':',ans[h][0],ans[h][1]
