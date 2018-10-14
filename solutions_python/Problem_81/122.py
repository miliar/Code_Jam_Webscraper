import sys

T=int(sys.stdin.readline())


for case in range(T):
	print "Case #%d:" % (case+1)
	N=int(sys.stdin.readline())
	S = []
	for l in range(N):
		S.append(sys.stdin.readline().strip())
	WP = [(0,0)] * N
	OWP = [0] * N
	OOWP = [0] * N
	for ta in range(N):
		l = S[ta]
		for tb in range(N):
			res = l[tb]
			if res != '.':
				res = int(res)
				o = WP[ta]
				WP[ta] = (o[0] + 1, o[1]+res)

	for ta in range(N):
		l = S[ta]
		ow = 0
		ops = 0
		for tb in range(N):
			res = l[tb]
			if res != '.':
				o = WP[tb]
				res = int(res)
				ow += float(o[1] - (1-res)) / (o[0] - 1)
				ops += 1
		OWP[ta] = ow / ops

	for ta in range(N):
		l = S[ta]
		ow = 0
		ops = 0
		for tb in range(N):
			res = l[tb]
			if res != '.':
				ow += OWP[tb]
				ops += 1
		OOWP[ta] = ow / ops
				
#	print WP, OWP, OOWP
	for t in range(N):
		RPI = (0.25 * WP[t][1]) / WP[t][0] + 0.50 * OWP[t] + OOWP[t]*0.25
		print RPI
	