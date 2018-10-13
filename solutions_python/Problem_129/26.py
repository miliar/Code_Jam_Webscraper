class emp: pass

for test in range(input()):
	N,M = map(int,raw_input().split())
	V = [None]*(M*2)
	Vt = []
	for i in range(M):
		o,e,p = map(int,raw_input().split())
		Vt += [(o,e,p)]
		V[i*2] = (o,-p)
		V[i*2+1] = (e,p)
	V.sort()
	# print V
	C = 0
	for v in Vt:
		d = v[1]-v[0]
		C += v[2]*(N*d-d*(d+1)/2)
	T = []
	for v in V:
		# print T,v
		if v[1]<0:
			T += [[v[0],-v[1]]]
		else:
			T.sort()
			n = v[1]
			while n>0:
				t = min(n,T[-1][1])
				if T[-1][0]!=v[0]:
					d = v[0]-T[-1][0]
					C -= t*(N*d-d*(d+1)/2)
				n -= t
				T[-1][1] -= t
				if T[-1][1]==0:
					del T[-1]
	C %= 1000002013
	print "Case #%s: %s"%(test+1,C)
