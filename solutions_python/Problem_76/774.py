#!/usr/bin/env python3

import sys
from functools import reduce

T = int(sys.stdin.readline())

for test in range(T):
	N = int(sys.stdin.readline())
	C = list(map(int, sys.stdin.readline().split()[:N]))
	if reduce(lambda x,y: x^y, C) == 0:
		print('Case #{}: {}'.format(test+1, sum(C)-min(C)))
	else:
		print('Case #{}: NO'.format(test+1))
