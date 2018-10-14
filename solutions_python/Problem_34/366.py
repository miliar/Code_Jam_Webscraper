#!/usr/bin/env python

import string
import re

with open('in.txt') as f:
	L, D, N = [int(i) for i in f.readline().strip().split()]
	words = [f.readline().strip() for i in xrange(D)]
	patterns =  [f.readline().strip().translate(string.maketrans('()', '[]'))
	             for i in xrange(N)]

patterns = map(re.compile, patterns)

with open('out.txt', 'w') as f:
	for case, pattern in enumerate(patterns):
		print >>f, 'Case #%d: %d' % (case+1,
			len(filter(lambda word: pattern.match(word) is not None, words)))
