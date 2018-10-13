import sys

cases = int(raw_input())
for case in range(1, cases + 1):
	R, C, D = map(int, raw_input().split(' '))
	#print R, C, D

	m = []
	for i in xrange(R):
		m.append(map(int, raw_input()))

	def best():
		for k in xrange(min(R, C) + 1, 3 - 1, -1):
			for i in xrange(R - k + 1):
				for j in xrange(C - k + 1):
					d = (k - 1) / 2.0
					cx = i + d
					cy = j + d
					#print i, j, k

					mx, my = 0, 0
					for a in xrange(k):
						for b in xrange(k):
							if not((b == 0 or b == k - 1) and (a == 0 or a == k - 1)):
								mass = m[i + a][j + b]
								mx += mass * (i + a - cx)
								my += mass * (j + b - cy)
								#print '---->', i + a, j + b, mass
						
					#print k, i, j, cx, cy, mx, my
					if mx == 0 and my == 0:
						return k

		return -1

	max = best()
	sys.stdout.write("Case #%d: %s\n" % (case, max if max > 0 else 'IMPOSSIBLE'))

