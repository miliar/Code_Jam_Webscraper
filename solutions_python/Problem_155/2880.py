#! /usr/bin/env python
"""
Name: Sravan Bhamidipati
Date: 11th April, 2015
Purpose: https://code.google.com/codejam/contest/6224486/dashboard#s=p0
"""

import sys

with open(sys.argv[1]) as fd:
	for line_no, line in enumerate(fd):
		if line_no == 0:
			continue
		else:
			invite = 0
			clapping = 0
			for level, members in enumerate(line.split()[1]):
				members = int(members)
				required = level - clapping
				if required > 0:
					invite += required
					clapping += required
				clapping += members
			print 'Case #%s: %s' % (line_no, invite)
