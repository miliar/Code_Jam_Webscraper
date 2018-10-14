#!/usr/bin/env python
import math

num_cases = int(raw_input())  # read a line with a single integer

cases = [raw_input() for _ in xrange(num_cases)]

for x, case in enumerate(cases):
	
	stalls, people = case.split(' ')
	stalls, people = int(stalls), int(people)

	l, r = stalls, stalls
	next = l
	while people > 0:


		l, r = int(math.ceil((next - 1) / 2.0)), int(math.floor((next - 1) / 2.0))
		next = l if people % 2 == 0 else r
		people = int(math.ceil((people - 1)/2.0))


	print 'Case #{}: {} {}'.format(x+1, l, r)
