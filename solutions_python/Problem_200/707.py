T=int(input())
for t in range(T):
	v = 0
	N=int(input())
	if N % 10 == 0:
		N -= 1
	M = map(int, str(N))
	low = 0
	high = 1
	for i in range(1,len(M)):
		low = low * 10 + 9
		high = high * 10 + 1
	if N>=low and N<high:
		v = low
	else:
		found = 1
		while found > 0:
			found = 0
			for i in range(1,len(M)):
				if found > 0:
					M[i] = '9'
				else:
					if M[i] < M[i-1]:
						found = 1
						M[i-1] -= 1
						M[i] = 9
		v = int(''.join(map(str,M)))
	print("Case #%d: %d"%(t+1,v))
