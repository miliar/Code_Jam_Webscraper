import copy

t = int(raw_input())
for i in xrange(t):
	rkn = map(int, raw_input().split())
	R = rkn[0]
	K = rkn[1]
	N = rkn[2]
	gl = map(int, raw_input().split())

	y = 0

	wq = []
	wq += gl
	for j in xrange(R):
		rq = []
		places = K

		k = 0
		while k < len(wq):
			if wq[k] <= places:
				rq.append(wq[k])
				places -= wq[k]
				del wq[k]
			else:
				#k += 1
				break
		
		y += (K - places)
		for l in rq:
			wq.append(l)

		#print rq


	print 'Case #%i: %i' % (i+1, y)
