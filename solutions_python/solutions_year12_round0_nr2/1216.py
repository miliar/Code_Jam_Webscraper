from __future__ import print_function
from math import ceil

path = 'B-large'

input = open(path + '.in')
output = open(path + '.out', 'w')

T = int(input.readline())
for t in range(T):
	N, S, p, *data = [int(d) for d in input.readline()[:-1].split(' ')]
	c = 0

	for o in data:
		d = ceil(o / 3)
		if d >= p:
			c += 1
		elif S > 0 and d == p - 1 and o % 3 in [0, 2] and o > 0:
				c += 1
				S -= 1

	print('Case #{t}: {c}'.format(t = t + 1, c = c), file = output)
