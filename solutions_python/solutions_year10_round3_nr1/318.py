t = int(raw_input())
for i in xrange(t):
	n = int(raw_input())
	AB = []
	xc = 0
	for j in xrange(n):
		ai, bi = map(int, raw_input().split())
		
		for k in xrange(j):
			ak, bk = AB[k]

			dv = (bi - ai - bk + ak)
			if dv == 0:
				continue
			xx = float(ak - ai) / dv
			if xx > 0 and xx < 1:
				xc += 1

		AB.append((ai, bi))



	print 'Case #%i: %i' % (i+1, xc)
