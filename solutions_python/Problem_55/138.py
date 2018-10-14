TESTCASES = int(raw_input())

for CASE in range(TESTCASES):
	# R=runs, K=size, N=groups
	(R,K,N) = map(int, raw_input().split(' '))
	G = map(int, raw_input().split(' '))

	E = 0
	if sum(G) <= K:
		E = R*sum(G)
		R=0

	if R > 0:
		RIDERS = [0]*N
		LOOP = [0]*N
		for P in range(N):
			PE = P
			T = 0
			while G[PE] <= K-T:
				T += G[PE]
				PE = (PE+1) % N
			RIDERS[P] = T
			LOOP[P] = PE

		# Pos = 0, Taken = 0
		P = 0
		RIDE = {}
		RN = 0
		while R > 0:
			if P in RIDE:
				TR = RN - RIDE[P][0]
				if R > TR:
					diff = E - RIDE[P][1]
					nt = int(R / TR)
					R -= nt * TR
					E += diff * nt
					RN += nt * TR
					if R == 0: break
			RIDE[P] = (RN,E)
			E += RIDERS[P]
			P = LOOP[P]
			R = R-1
			RN = RN + 1


  
	
	print "Case #%d: %d" % (CASE+1, E)
