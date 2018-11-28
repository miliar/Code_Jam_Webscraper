from heapq import *

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  N, people = [int(s) for s in input().split(" ")]
  h = []
  heappush(h, 0)
  while people:
      people -= 1
      biggestSpace = N - heappop(h)
      if biggestSpace % 2 == 1:
          if people == 0:
              result = [int(biggestSpace/2)]
          heappush(h, N - int(biggestSpace/2))
          heappush(h, N - int(biggestSpace/2))
      else:
          if people == 0:
              result = [(int(biggestSpace/2) - 1), int(biggestSpace/2)]
          heappush(h, N - (int(biggestSpace/2) - 1))
          heappush(h, N - int(biggestSpace/2))
  print("Case #{}: {} {}".format(i, max(result), min(result)))