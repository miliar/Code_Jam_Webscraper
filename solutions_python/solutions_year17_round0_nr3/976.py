from heapq import heappush, heappop

x = int(input())
for num in range(1, x + 1):
  curr = input()
  n = int(curr.split(' ')[0])
  k = int(curr.split(' ')[1])
  q = []
  heappush(q, n * -1)
  for i in range(0, k):
    stalls = heappop(q) * -1
    if stalls % 2 == 0:
      maxS = stalls // 2
      minS = maxS - 1
    else:
      minS = maxS = (stalls - 1) // 2
    heappush(q, minS * -1)
    heappush(q, maxS * -1)
  print("Case #" + str(num) + ": " + str(maxS) + " " + str(minS))
  
