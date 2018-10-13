#!/usr/bin/env python

def test(s):
	#print s
	p = 0
	f = 0
	for i, c in enumerate(s):
		#print "%d: %d necessarios %d ja de pe." % (i, i, p),
		if p >= i:
			p = p + c
			#print "Ja tem suficiente %d levantam." % (c) 
		else:
			a = i-p
			f += a
			p += a + c
			#print "Adicionou %d amigos" % (a)
		#print "Amigos: %d" % (f)
	return f

#print test([0, 0, 2, 0, 0, 0, 1])
t = int(raw_input(''))
for c in range(1, t+1):
	max, s = raw_input('').split()
	max = int(max)
	s = map(int, list(s))
	print 'Case #%d: %d' % (c, test(s))