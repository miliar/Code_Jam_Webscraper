#!/usr/bin/python2.7

for case in range(input()):
	data = raw_input().split()
	sol = 0
	stand = 0
	for i in xrange(int(data[0])+1):
		if (int(data[1][i]) != 0):
			if (stand < i):
				sol += i - stand
				stand = i
			cur = int(data[1][i])
			stand += cur

	print 'Case #%s: %s' % ((case + 1), sol)

