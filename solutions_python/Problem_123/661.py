#!/usr/bin/python3

import sys

def solve(a, m, i):
	if i >= len(m):
		return 0
	operations = 0
	if m[i] < a:
		return solve(a + m[i], m, i+1)
	else:
		if a != 1:
			b = min(solve(a*2 -1, m, i), solve(a, m, i+1))
		else:
			b = solve(a, m, i+1)
		operations = b + 1
	return operations
				

T = int(sys.stdin.readline().strip())
for i in range(0, T):
	a, n = [int(z) for z in sys.stdin.readline().strip().split(" ")]
	motes = [int(z) for z in sys.stdin.readline().strip().split(" ")]
	motes = sorted(motes)
	operations = solve(a, motes, 0)
	print ("Case #{}: {}".format(i+1, operations))

