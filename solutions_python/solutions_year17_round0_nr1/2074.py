#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
	f.next()
	for case, line in enumerate(f, 1):
		pancakes, width = line.strip().split()
		width = int(width)
		pancakes = map(lambda x: x == '+', pancakes)
		flips = 0
		while True:
			try:
				unflipped = pancakes.index(False)
			except ValueError:
				break
			pancakes = pancakes[unflipped:]
			if width > len(pancakes) \
			or width == len(pancakes) and True in pancakes:
				flips = 'IMPOSSIBLE'
				break
			for i in range(width):
				pancakes[i] = not pancakes[i]
			flips += 1
		print 'Case #%s: %s' % (case, flips)
