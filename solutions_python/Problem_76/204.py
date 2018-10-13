#! /usr/bin/env python3
import functools, operator
T = int(input())
for i in range(T):
	N = int(input())
	C = tuple(map(int, input().split()))
	if functools.reduce(operator.xor, C):
		ans = 'NO'
	else:
		ans = sum(C) - min(C)
	print('Case #%d: %s' % (i+1, ans))