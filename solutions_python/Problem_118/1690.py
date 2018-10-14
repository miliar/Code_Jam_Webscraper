import math

def isPal(x):
	return str(x) == str(x)[::-1]

def solve(a, b):
	a, b = int(a), int(b)

	count = 0
	for i in xrange(1, int(math.ceil(math.sqrt(b))) + 1):
		if i * i >= a and i * i <= b:
			if isPal(i) and isPal(i * i):
				count += 1
	return count

import sys

for t, line in enumerate(sys.stdin.readlines()[1:]):
	count = solve(*line.rstrip().split(' '))
	print 'Case #%d:' % (t+1), count