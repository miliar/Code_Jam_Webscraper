from heapq import *
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  N, K = [int(x) for x in input().split(' ')]
  h = []
  heappush(h, -N)
  for j in range(K-1):
    len = -heappop(h)
    lmin = (len-1) // 2
    lmax = (len-1) - lmin
    heappush(h, -lmin)
    heappush(h, -lmax)
  len = -heappop(h)
  lmin = (len - 1) // 2
  lmax = (len - 1) - lmin
  result = ' '.join([str(lmax), str(lmin)])
  print("Case #{}: {}".format(i, result))
