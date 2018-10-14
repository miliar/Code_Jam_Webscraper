#!/usr/bin/env python3

# Cookie clicker

# Start with 0 cookies
# 2 cookies/sec by clicking on a giant cookie
# Having C cookies, you buy a cookie farm
# A cookie farm costs C cookies and gives +F cookies/sec
# You with with X cookies not spent on farms

# How long it will take you to win using the best possible strategy?


# Input
# First line: test cases T

import sys

# First line the number of test cases T
T = int(sys.stdin.readline())

def solve(C, F, X):
	speed = 2 # We start with 2 cookies/sec
	time = 0 # Time required to reach X
	while True:
		# Time to reach X at current speed
		tx = X / speed
		# Time to reach the next farm
		tc = C / speed
		# Time to reach X using the farm
		tf = tc + X / (speed + F)
		# Check which is faster
		if tf < tx:
			speed += F
			time += tc
		else:
			break # Current speed is the best possible
	return time + X / speed

for t in range(T):
	C, F, X = [float(x) for x in sys.stdin.readline().split()]
	
	tottime = solve(C, F, X)

	print("Case #{}: {}".format(t + 1, tottime))

