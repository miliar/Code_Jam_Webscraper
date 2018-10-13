#!/usr/bin/python

T = int(raw_input())
for test in xrange(T):
	n = int(raw_input().split()[0])
	a = []
	for i in xrange(n):
		a.append(raw_input())
		a[i] += '.'
	a.append('.' * (len(a[0])))
#	print a

	pos = True
	m = len(a[0])
	for i in xrange(n):
		for j in xrange(m):
			if a[i][j] == '#':
				if a[i][j+1] == '#' and a[i+1][j] == '#' and a[i+1][j+1] == '#':
					a[i] = a[i][:j] + "/\\" + a[i][j+2:]
					a[i+1] = a[i+1][:j] + "\\/" + a[i+1][j+2:]
				else:
					pos = False

	print "Case #%d:" % (test + 1)
	if not pos:
		print "Impossible"
	else:
		for i in xrange(n):
			print a[i][:-1]

#	print "Case #%d: %d" % (test + 1, time)
