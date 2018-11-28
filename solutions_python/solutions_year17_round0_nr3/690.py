T=int(input())
for t in range(T):
	P=map(int, raw_input().split())
	c = 0
	A=[]
	A.append([P[0],1])
	while c < P[1]:
		A.sort(reverse=True)
		if len(A) > 1:
			if A[0][0] == A[1][0]:
				A[1][1] += A[0][1]
				del A[0]
		a = A[0][0] - 1
		b = A[0][1]
		c += b
		r = int( a / 2 )
		l = a - r
		if r == l:
			A[0] = [ r, b * 2 ]
		else:
			A.append([ r, b ])
			A[0]=[ l, b ]
	print("Case #%d: %d %d"%(t+1,l,r))
