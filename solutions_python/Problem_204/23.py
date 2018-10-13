#!/usr/bin/env python
from fractions import Fraction
import math
import sys

if __name__ == '__main__':
	T = int(sys.stdin.readline())
	for t in range(1, T+1):
		N, P = list(map(int, sys.stdin.readline().strip().split()))
		R = list(map(int, sys.stdin.readline().strip().split()))
		Q = [sorted(map(Fraction, sys.stdin.readline().strip().split())) for n in range(N)]
		for n in range(N):
			for p in range(P):
				Q[n][p] /= R[n]
		indices = [0] * N
		kits = 0
		while max(indices) < P:
			values = [Q[n][indices[n]] for n in range(N)]
			max_servings = math.floor(min(values) * Fraction(10, 9))
			min_servings = math.ceil(max(values) * Fraction(10, 11))
			if min_servings <= max_servings:
				kits += 1
				indices = [i+1 for i in indices]
			else:
				indices[values.index(min(values))] += 1
		print('Case #%d: %d' % (t, kits))
