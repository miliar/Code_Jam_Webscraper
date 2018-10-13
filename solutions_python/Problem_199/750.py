#!/usr/bin/env python3

from sys import stdin

def solve(ifs):
  cakes, width = ifs.readline().strip().split(' ')
  width = int(width)
  cakes = [ch for ch in cakes]
  n_flips = 0
  for i in range(len(cakes) + 1 - width):
    if cakes[i] == '-':
      n_flips += 1
      for j in range(i, i + width):
        cakes[j] = '+' if cakes[j] == '-' else '-'

  if any(cake == '-' for cake in cakes):
    return 'IMPOSSIBLE'
  else:
    return str(n_flips) 

if __name__ == '__main__':
	T = int(stdin.readline())
	#print(T, 'cases to evaluate')
	for i in range(T):
		result = solve(stdin)
		print('Case #' + str(i + 1) + ': ' + result)
