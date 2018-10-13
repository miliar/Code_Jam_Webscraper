class streamreader:
	def __init__(_,s): _.t=(t for t in s.read().split())
	def __div__(_,t): return (t)(_.t.next())

import sys
sr = streamreader(sys.stdin)

for tc in xrange(sr/int):
	R, C, D = sr/int, sr/int, sr/int
	m = []
	for y in xrange(R):
		m.append( [D + int(x) for x in sr/str] )
		
	def solve(K):
		for y0 in xrange(R - K + 1):
			for x0 in xrange(C - K + 1):
				xm = 0
				ym = 0
				mass = 0
				for y in xrange(K):
					for x in xrange(K):
						if (x == 0 and y == 0) or (x == K-1 and y == 0) or (x == 0 and y == K-1) or (x == K-1 and y == K-1):
							continue
						_m = m[y + y0][x + x0]
						mass += _m
						xm += (x + 1) * _m
						ym += (y + 2) * _m
				#print x0, y0, xm, ym, mass
				if (2*xm % mass == 0 and 2*ym % mass == 0):
					return True
		return False
	
	answer = 'IMPOSSIBLE'
	
	K = min(R, C)
	while K >= 3:
		solved = solve(K)
		if solved:
			answer = K
			break
		else:
			K -= 1
	
	print 'Case #%d:' % (tc + 1), answer