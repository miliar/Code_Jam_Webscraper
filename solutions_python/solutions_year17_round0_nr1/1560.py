#!/usr/bin/env python
num_cases = int(raw_input())  # read a line with a single integer

cases = [raw_input() for _ in xrange(num_cases)]

for i, case in enumerate(cases):
	cakes, size = case.split(' ')
	size = int(size)
	cakes = [c for c in cakes]

	result = 0
	while len(cakes) >= size:
		cur = cakes.pop(0)
		if cur == '-':
			result += 1
			for j in xrange(size - 1):
				cakes[j] = '+' if cakes[j] == '-' else '-'

	
	if '-' in cakes:
		result = 'IMPOSSIBLE'

	print 'Case #{}: {}'.format(i+1, result)
