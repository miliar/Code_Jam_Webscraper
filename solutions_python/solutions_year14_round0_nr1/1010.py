#! /usr/bin/env python
'''
Name: Sravan Bhamidipati
Date: 11th April, 2014
Purpose: 
'''

import sys

with open(sys.argv[1]) as fd:
	for line_no, line in enumerate(fd):
		rem = line_no % 10

		if line_no == 0:
			continue
		elif rem == 1:
			layout1 = []
			layout2 = []
			answer1 = int(line.strip()) - 1
		elif 2 <= rem <= 5:
			layout1.append(line.strip().split())
		elif rem == 6:
			answer2 = int(line.strip()) - 1
		else:
			layout2.append(line.strip().split())

			if len(layout2) == 4:
				case = line_no / 10
				common = frozenset(layout1[answer1]) & frozenset(layout2[answer2])

				if len(common) == 0:
					print 'Case #%d: Volunteer cheated!' % case
				elif len(common) > 1:
					print 'Case #%d: Bad magician!' % case
				else:
					print 'Case #%d: %s' % (case, ''.join(common))

