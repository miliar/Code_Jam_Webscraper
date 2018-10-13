#!/usr/bin/env python3

from sys import stdin
from math import pi

def solve(ifs):
  N, K = [int(v) for v in ifs.readline().strip().split(' ')]
  pancakes = [(int(p[0]), int(p[1])) 
              for p in (ifs.readline().strip().split(' ') for i in range(N))]
  pancakes.sort(key=lambda p: -p[0])
  areas = [pi*p[0]*(p[0] + 2*p[1]) for p in pancakes]

  for k in range(1, K):
    next_areas = [0.0 for p in pancakes]
    for i in range(k, N):
      curr_cake = pancakes[i]
      next_areas[i] = max(areas[j] + 2*pi*curr_cake[0]*curr_cake[1] 
                          for j in range(k-1, i))

    areas = next_areas

  return str(max(areas))

if __name__ == '__main__':
	T = int(stdin.readline())
	#print(T, 'cases to evaluate')
	for i in range(T):
		result = solve(stdin)
		print('Case #' + str(i + 1) + ': ' + result)
