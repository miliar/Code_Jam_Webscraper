#!/usr/bin/env python

with open('A-large.in') as f:
	cases = int(f.readline())

	for caseNum in range(1, cases+1):
		problem = [tok for tok in f.readline().split()]
		sm = int(problem[0])
		row = [int(s) for s in problem[1]]

		standing = row[0]
		added = 0
		for shyness in range(1, sm+1):
			if standing < shyness:
				add = (shyness - standing)
				standing += add
				added += add
			standing += row[shyness]

		print("Case #{0}: {1}".format(caseNum, added))
