#!/usr/bin/python
# coding: utf-8

import sys, itertools



if __name__ == "__main__":
	mp = dict()
	for a, b in itertools.izip(open('a.in'), open('a.out')):
		a = a.rstrip('\n')
		b = b.rstrip('\n')
		b = b[9:] # Warning, max 9 cases
		if len(a) != len(b):
			sys.stderr.write("Warning: different length in «%s» <<-- «%s»\n" % (a,b))
		for ca,cb in itertools.izip(a,b):
			if ca in mp and mp[ca] != cb:
				sys.stderr.write("Warning: Invalid mapping, %s --> %s, but was %s before, at «%s» --> «%s»\n" % (ca,cb, mp[ca], a, b))
			mp[ca] = cb
	mp['\n'] = '\n'
	# for x in sorted(mp.values()):
		# print x
	mp['z'] = 'q' # Fuck!

	# print mp
	# Solve
	n = int(raw_input().rstrip('\n'))
	for i in range(n):
		s = raw_input().rstrip('\n')
		r = ''.join(mp[x] for x in s)
		print 'Case #%d: %s' % (i+1, r)
