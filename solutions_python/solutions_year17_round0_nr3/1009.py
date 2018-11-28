import sys

import heapq

cases = int(input())
for case in range(cases):
  print("On case {}".format(case), file = sys.stderr)
  stalls, people = list(map(int, input().split()))
  
  while people % 2 == 0 and stalls % 2 == 0:
    stalls //= 2
    people //= 2
    
  heap = [-stalls]
  heapq.heapify(heap)
  
  for x in range(people - 1):
    value = -heapq.heappop(heap)
    if value % 2 == 0:
      heapq.heappush(heap, -value / 2)
      heapq.heappush(heap, -(value / 2 - 1))
    else:
      heapq.heappush(heap, -(value // 2))
      heapq.heappush(heap, -(value // 2))
    #print(list(maxh))
      
  value = -heapq.heappop(heap)
  if value % 2 == 0:
    bestMax = value / 2
    bestMin = value / 2 - 1
  else:
    bestMax = value // 2
    bestMin = bestMax

  print("Case #{}: {} {}".format(case + 1, int(bestMax), int(bestMin)))