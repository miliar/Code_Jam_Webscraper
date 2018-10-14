#! /usr/bin/python

import sys
from collections import defaultdict

f = open(sys.argv[1], 'rt')

for t in range(1, int(f.readline())+1):
	l = f.readline().split(' ').__iter__()
	
	c = {}
	d = defaultdict(list)

	for i in range(int(l.next())):
		x = l.next()
		c[frozenset( (x[0], x[1]) )] = x[2]

	for i in range(int(l.next())):
		x = l.next()
		d[x[0]].append(x[1])
		d[x[1]].append(x[0])

	l.next()
	r = []
	for ch in l.next().strip():
		if r == []:
			r.append(ch)
		elif frozenset( (r[-1], ch) ) in c:
			r[-1] = c[frozenset( (r[-1], ch) )]
		else:
			for x in d[ch]:
				if x in r:
					r = []
					break
			else:
				r.append(ch)

	s = '[' + ', '.join(r) + ']' 
	print "Case #%d: %s" % (t, s)
