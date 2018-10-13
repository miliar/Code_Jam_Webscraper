#! /usr/bin/env python

from __future__ import print_function
from sys import stdin, stderr
import math


debug = True

def debug_print(s):
	if debug:
		print('    DEBUG: {}'.format(s), file=stderr)


def solve(C, F, X):
	p = (X / C) - (2 / F)
	p_floor = math.trunc(p) if p > 0 else 0
	t = sum([(C / (2 + (F * i))) for i in range(int(p_floor))])
	n = X / (2 + (F * p_floor))
	z = t + n
	debug_print('  p: {}, p_floor: {}, t: {}, n: {}'.format(p, p_floor, t, n))
	return z


if __name__ == '__main__':
	num_cases = int(stdin.readline().strip())

	for case in range(1, num_cases + 1):
		C, F, X = [float(x) for x in stdin.readline().strip().split()]
		debug_print('  C: {}, F: {}, X: {}'.format(C, F, X))

		out = solve(C, F, X)
		print('Case #{}: {}'.format(case, out))

