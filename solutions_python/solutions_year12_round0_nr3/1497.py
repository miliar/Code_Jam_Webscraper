#!/usr/bin/env python

import sys

rl = sys.stdin.readline
rot = lambda x: [int('%s%s' % (x[-z:], x[:-z])) for z in xrange(1, len(x))]
worth = lambda n, m: sorted(str(n)) == sorted(str(m))
cache = { }

for nr in range(int(rl().strip())):
	a, b = map(int, rl().strip().split())
	result = 0

	for n in xrange(a, b + 1):
		for m in xrange(n + 1, b + 1):
			if worth(n, m):
				em = str(m)
				c = cache.get(em, {})

				if not c:
					c = rot(em)
					cache.update({em: c})

				result += n in c

	print 'Case #%d: %s' % (nr + 1, result)
