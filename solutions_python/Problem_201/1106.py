from heapq import *
for t in range(input()):
  n, k = map(int, raw_input().split())
  q = [-n]
  for _ in range(k):
    x = abs(heappop(q))
    heappush(q, -(x/2))
    heappush(q, -((x-1)/2))
  print('Case #%d: %d %d' % (t+1, x/2, (x-1)/2))
    
