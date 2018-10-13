import numpy as np
from heapq import heappush, heappop

def MyFunc(pancakes, K):
  pancakes.sort()
  N = len(pancakes)
  pq = []
  for i in range(K - 1):
    heappush(pq, 2 * pancakes[i][0] * pancakes[i][1])
  maxSoFar = 0
  for i in range(K - 1, N):
    # Choose pancakes[i]
    R, H = pancakes[i]
    curr = R * R + 2 * R * H
    for j in range(K - 1):
      curr += pq[j]
    if curr > maxSoFar: maxSoFar = curr
    heappush(pq, 2 * R * H)
    heappop(pq)
  return maxSoFar

if __name__ == '__main__':
  T = int(input())
  for i in range(1, T + 1):
    N, K = map(int, input().split(' '))
    pancakes = []
    for j in range(N):
      R, H = map(int, input().split(' '))
      pancakes.append((R, H))
    output = MyFunc(pancakes, K)
    output *= np.pi
    print('Case #{}: {}'.format(i, output))
