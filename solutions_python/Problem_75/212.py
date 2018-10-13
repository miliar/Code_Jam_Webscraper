#!/usr/bin/python
import sys
tests = int (sys.stdin.readline ())
for test in range (1, tests + 1):
	s = sys.stdin.readline ().split ()

        a = []
	c = int (s[0])
	for i in range (1, c + 1):
		t = s[i]
		a.append (((t[0], t[1]), t[2]))
		a.append (((t[1], t[0]), t[2]))
	a = dict (a)

        b = []
	d = int (s[c + 1])
	for i in range (c + 2, c + d + 2):
		t = s[i]
		b.append ((t[0], t[1]))
		b.append ((t[1], t[0]))
	b = set (b)

	assert c + d + 4 == len (s)
	k = int (s[-2])
	t = s[-1]
	assert k == len (t)
	p = []
	for e in t:
		p.append (e)
		if len (p) >= 2:
			f = (p[-1], p[-2])
			if f in a:
				p = p[:-2] + [a[f]]
			g = p[-1]
			for e in p:
				if (g, e) in b:
					p = []
					break
	print 'Case #%d:' % (test),
	s = '['
	for e in p:
		s += '%s, ' % e
	if s[-2:] == ', ':
		s = s[:-2]
	s += ']'
	print s
