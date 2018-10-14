#!/usr/bin/env python3

import sys

T = int(sys.stdin.readline())

for t in range(T):
	N, L, H = tuple(map(int, sys.stdin.readline().strip().split()))
	F = list(map(int, sys.stdin.readline().strip().split()))
	for i in range(L, H+1):
		for f in F:
			if f % i and i % f:
				break
		else:
			print('Case #{}: {}'.format(t+1, i))
			break
	else:
		print('Case #{}: NO'.format(t+1))
