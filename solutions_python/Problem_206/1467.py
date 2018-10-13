#!/usr/bin/env python3

from sys import stdin

def solve(ifs):
  D, N = [int(v) for v in ifs.readline().strip().split(' ')]
  horses = [(float(v[0]), float(v[1])) 
            for v in (ifs.readline().strip().split(' ') for i in range(N))]
  t_reach = [(D - h[0]) / h[1]  for h in horses]
  #print(t_reach)

  return str(D / max(t_reach))

if __name__ == '__main__':
	T = int(stdin.readline())
	#print(T, 'cases to evaluate')
	for i in range(T):
		result = solve(stdin)
		print('Case #' + str(i + 1) + ': ' + result)
