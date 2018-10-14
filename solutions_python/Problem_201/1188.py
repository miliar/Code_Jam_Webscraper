import heapq as hq


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  h = []
  n, k = [int(x) for x in input().split(" ")]
  
#  if k - 1 > n // 2:
##      if k == n:
#      print("Case #{}: {} {}".format(i, 0, 0))
##      else:
##          print("Case #{}: {} {}".format(i, 1, 0))
#      continue
  
  hq.heappush(h, -n)
  
  for j in range(k):
      a = hq.heappop(h)
      
      b1 = (a + 2) // 2
      b2 = (a + 1) // 2
           
      hq.heappush(h, b1)
      hq.heappush(h, b2)
  
  l1 = -b1
  l2 = -b2
  
  print("Case #{}: {} {}".format(i, max(l1,l2), min(l1,l2) ))