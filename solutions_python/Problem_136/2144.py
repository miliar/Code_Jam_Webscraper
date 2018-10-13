T = int(raw_input())

for t in range(T):
	C, F, X = [float(i.strip()) for i in raw_input().split()]
	
	N = max(int((X*F - 2*C)/(C*F)),0)

	res = 0
	for n in range(N):
		res += C/(2+n*F)
	res += X/(2+N*F)

	print 'Case #%d: %s' % (t+1, res)