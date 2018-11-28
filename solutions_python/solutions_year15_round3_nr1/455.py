import sys
import os

T = int(sys.stdin.readline().strip())

for t in xrange(T):
	R, C, W = map(int, sys.stdin.readline().strip().split())

	if C%W == 0:
		ans = C/W + (W-1)
	else:
		ans = C/W + W

	ans = ans*R

	sys.stdout.write('Case #{0}: {1}\n'.format(t+1, ans))


