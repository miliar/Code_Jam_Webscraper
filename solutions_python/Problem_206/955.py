cs = 1
T = int(input())

while T:
	T-= 1

	[D, N] = [int(k) for k in input().split()]
	H = 0.0
	
	for k in range(N):
		x = [float(t) for t in input().split()]
		if (float(D) - x[0])/x[1] > H:
			H = (float(D) - x[0])/x[1]

	print('Case #' + str(cs) + ': ', end = '')
	print('%.6f' % round(D/H, 6))

	cs += 1