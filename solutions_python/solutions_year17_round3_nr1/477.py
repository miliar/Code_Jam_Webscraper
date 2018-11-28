
import sys
from math import pi

T = int(sys.stdin.readline())

for t in range(1, T + 1):
  N, K = [int(x) for x in sys.stdin.readline().split()]
  pancakes = []
  for i in range(N):
    r, h = [int(x) for x in sys.stdin.readline().split()]
    pancakes.append((r, h))
  pancakes.sort(reverse=True)
  best = 0.0
  for i in range(N - K + 1):
    choice = [pancakes[i]] + sorted(pancakes[i + 1:], key=lambda x: x[0] * x[1], reverse=True)[:K-1]
    area = sum(2 * pi * r * h for r, h in choice) + pi * choice[0][0] ** 2
    if area > best:
      best = area
  print('Case #%d: %f' % (t, best))
  

