with open("B-large.in") as f:
	T = int(f.readline())
	for tt in range(0,T):
		C, F, X = [float(n) for n in f.readline().split(' ')]
		N = 1000000
		A = [0.0]*N
		for i in range(1,N):
			A[i] = A[i-1] + 1/(2+(i-1)*F)
		for i in range(0,N):
			A[i] = C*A[i] + X/(2+i*F)
		print("Case #{0}: {1}".format(tt+1, min(A)))