#!/usr/bin/env python
from itertools import combinations
def get_int_arr():
	return [int(x) for x in raw_input().split()]

def solve():
	N = get_int_arr()[0]
	vals = get_int_arr()
	sumall = sum(vals)

	# all possibilities
	max_sum = 0
	for i in range(1, 2**N-1):
		half = 0
		halfxor = 0
		anotherxor = 0
		for c in range(0, N):
			if (i & (1<<c)) > 0:
				half += vals[c]
				halfxor ^= vals[c]
			else:
				anotherxor ^= vals[c]
		if anotherxor == halfxor:
			if half > max_sum:
				max_sum = half
			if sumall-half > max_sum:
				max_sum = sumall-half
	if max_sum == 0:
		return 'NO'
	else:
		return max_sum
		
t = get_int_arr()[0]
for x in range(t):
	print 'Case #%d: %s' % (x+1, solve())
