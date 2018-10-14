#!/usr/local/bin/python2.7

with open('input.txt') as f:
	cases = int(f.readline().strip())
	# if not (1 <= cases <= 100):
	# 	raise ValueError('Invalid number of cases.')
	# Error handling omitted. Supposed input format is correct.
	for case in xrange(1, cases + 1):
		row1 = int(f.readline().strip())
		for i in xrange(1, 5):
			line = f.readline().strip()
			if i == row1:
				cards1 = [int(n) for n in line.split()]
		row2 = int(f.readline().strip())
		for i in xrange(1, 5):
			line = f.readline().strip()
			if i == row2:
				cards2 = [int(n) for n in line.split()]
		common = [i for i in cards1 if i in cards2]

		if len(common) == 1:
			print 'Case #%d: %d'%(case, common[0])
		elif len(common) > 1:
			print 'Case #%d: Bad magician!'%case
		else:
			print 'Case #%d: Volunteer cheated!'%case

