#!/usr/bin/python

import sys
rl = sys.stdin.readline

def result(mam, todo):
	res = 0

	for x in todo:
		if x not in mam:
			xx = x.split('/')

			for y in xrange(2, len(xx) + 1):
				xxx = '/' + '/'.join(xx[1:y])
				if xxx not in mam:
					res += 1
					mam.append(xxx)

	return res

for t in xrange(1, int(rl()) + 1):
	(n, m), mam, todo = map(int, rl().split()), [], []

	if n > 0:
		for N in xrange(1, n + 1):
			mam.append(rl().strip())

	for M in xrange(1, m + 1):
		todo.append(rl().strip())

	print 'Case #%d: %s' % (t, result(mam, todo))
