#!/usr/bin/env python

from __future__ import print_function
import sys

with open(sys.argv[1]) as f:
	for case in range(1, int(f.readline().strip()) + 1):
		cake = []
		for line in range(int(f.readline().strip().split()[0])):
			cake.append([l if l != '?' else '' for l in f.readline().strip()])
		print('Case #%s:' % case)
		previous_row = ''
		empty_rows = 0
		for row in cake:
			first_letter = ''.join(row)[:1]
			if not first_letter:
				if previous_row:
					print(previous_row)
				else:
					empty_rows += 1
			else:
				previous_row = ''
				for l in row:
					if l:
						first_letter = l
					previous_row += first_letter
				for i in range(empty_rows + 1):
					print(previous_row)
				empty_rows = 0

