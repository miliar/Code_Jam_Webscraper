#!/usr/bin/env python3

from sys import stdin
from heapq import heappush, heappop

def calc_stupid(N, K):
  segments = []
  heappush(segments, -N)

  while K > 0:
    n_free = -heappop(segments)
    n_free -= 1
    K -= 1

    mindist = n_free // 2
    maxdist = n_free - mindist

    if mindist > 0:
      heappush(segments, -mindist)

    if maxdist > 0:
      heappush(segments, -maxdist)

  return maxdist, mindist

def calc(N, K):
  N -= 1
  K -= 1

  if K == 0:
    mindist = N // 2
    maxdist = N - mindist

    return maxdist, mindist

  else:
    if N & 1:
      if K & 1:
        N_sub = (N // 2) + 1
        K_sub = (K // 2) + 1
      else:
        N_sub = N // 2
        K_sub = K // 2
    else:
      N_sub = N // 2
      if K & 1:
        K_sub = (K // 2) + 1
      else:
        K_sub = K // 2

    return calc(N_sub, K_sub)

def solve(ifs):
  N, K = [int(s) for s in ifs.readline().strip().split(' ')]
  maxdist, mindist = calc(N, K)#calc_stupid(N, K)

  return '%s %s' % (maxdist, mindist)

if __name__ == '__main__':
	T = int(stdin.readline())
	#print(T, 'cases to evaluate')
	for i in range(T):
		result = solve(stdin)
		print('Case #' + str(i + 1) + ': ' + result)
