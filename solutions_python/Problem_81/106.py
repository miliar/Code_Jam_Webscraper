class streamreader:
	def __init__(_,s): _.t=(t for t in s.read().split())
	def __div__(_,t): return (t)(_.t.next())

import sys
sr = streamreader(sys.stdin)

for tc in xrange(sr/int):
	n = sr/int
	m = [sr/str for i in xrange(n)]
	
	wp = [0] * n
	
	for t in xrange(n):
		w = m[t].count('1')
		l = m[t].count('0')
		wp[t] = 1.0 * w / (w + l)
		
	owp = [0] * n
	
	for t in xrange(n):
		s, c = 0.0, 0
		for o in xrange(n):
			if o != t and m[o][t] != '.':
				w = m[o].count('1')
				l = m[o].count('0')
				if m[o][t] == '1':
					w -= 1
				if m[o][t] == '0':
					l -= 1
				s += 1.0 * w / (w + l)
				c += 1
		owp[t] = s / c
		
	oowp = [0] * n
	
	for t in xrange(n):
		s, c = 0.0, 0
		for o in xrange(n):
			if m[o][t] != '.':
				s += owp[o]
				c += 1
		oowp[t] =  s / c
		
	print 'Case #%d:' % (tc + 1)
	for t in xrange(n):
		print 0.25 * wp[t] + 0.5 * owp[t] + 0.25 * oowp[t]