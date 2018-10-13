T = input()

for i in range(T):
	N = raw_input()
	print 'Case #%s:' % (i + 1),
	
	L = len(N)
	for j in range(L - 1):
		if N[j] <= N[j + 1]:
			continue
		k = N.find(N[j])
		N = N[:k] + str(int(N[k]) - 1) 
		N += '9' * (L - k - 1)
		if N[0] == '0':
			N = N[1:]
		break
	print N

