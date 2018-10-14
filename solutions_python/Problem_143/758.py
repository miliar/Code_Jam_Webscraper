#! /usr/bin/env python
'''
Name: Sravan Bhamidipati
Date: 3rd May, 2014
Purpose: 
'''

import itertools
import sys

def win_count(a, b, k):
	wins = 0

	for (i, j) in itertools.product(xrange(a), xrange(b)):
		if i & j < k: wins += 1

	return wins


with open(sys.argv[1]) as fd:
	for line_no, line in enumerate(fd):
		if line_no == 0:
			continue
		else:
			print 'Case #%d: %d' % (line_no, win_count(*map(int, line.split())))

