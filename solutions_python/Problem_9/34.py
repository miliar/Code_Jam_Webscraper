#!/usr/bin/env python
import sys, math

cases = int(raw_input())
for case in range(cases):
	k = int(raw_input())
	ids = map(int, raw_input().split(' '))[1:]

	deck = [0]*(k + 1)
	next_free = range(1, k + 2)
	next_free[k] = 1

	n_gaps = k
	count = 0
	pos = 1
	next = 1
	last_link = k
	while 1:
		assert deck[pos] == 0
		count += 1
		if count == next:
			deck[pos] = next
			n_gaps -= 1
			next_free[last_link] = next_free[pos]
			next += 1
			if not n_gaps: break
			n_cycles = int((next - 2) / n_gaps)
			count = n_cycles * n_gaps
		last_link = pos
		pos = next_free[pos]

	selected = [deck[x] for x in ids]
	
	print "Case #%d: %s" % (case + 1, ' '.join(map(str, selected)))
