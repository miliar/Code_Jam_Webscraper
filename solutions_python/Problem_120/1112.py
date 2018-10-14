#!/usr/bin/env python3

import sys
from math import sqrt, pi

def number_of_circles(r, t):
	#k = (-(2 * r) + 1 + sqrt(((r * 2) -  1)**2 + (8 * t)/pi))/4
	delta = sqrt((((2 * r) - 1)**2) + (8 * t))
	k1 = (((-2 * r) + 1) + delta) / 4.0

	return int(k1)

if __name__ == '__main__':
	ncases = int(sys.stdin.readline())
	for case in range(ncases):
		r, t = [int(x) for x in sys.stdin.readline().strip().split(' ')]
		result = number_of_circles(r, t)
		print('Case #', case + 1, ': ', result, sep='')
