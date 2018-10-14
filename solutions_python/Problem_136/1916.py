#!/usr/bin/env python3

def read_ints():
	return map(int, input().strip().split())

def read_floats():
	return map(float, input().strip().split())

T, = read_ints()

def count_time(cps, goal):
	return goal/cps

for t in range(T):
	c, f, x = read_floats()

	cps = 2.
	spent = 0 # spent time
	res = count_time(cps, x)

	improved = True

	while improved:
		spent += count_time(cps, c)
		cps += f
		cur = spent + count_time(cps, x)

		if cur<res:
			res=cur
		else:
			improved = False

	print('Case #{}: {}'.format(t+1, res))
