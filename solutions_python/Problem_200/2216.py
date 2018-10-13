#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
	f.next()
	for case, line in enumerate(f, 1):
		limit = line.strip()
		for i in range(len(limit)):
			if i + 1 < len(limit) and limit[i] > limit[i+1]:
				break
		else:
			print 'Case #%s: %s' % (case, limit)
			continue
		for i in range(i, -1, -1):
			if i > 0 and int(limit[i]) - 1 < int(limit[i-1]):
				continue
			break
		else:
			if limit[0] == '1':
				print 'Case #%s: %s' % (case, (len(limit) - 1) * '9')
				continue
		largest = '%s%s%s' % (
			limit[:i],
			int(limit[i]) - 1,
			(len(limit) - i - 1) * '9',
		)
		print 'Case #%s: %s' % (case, largest.lstrip('0'))
