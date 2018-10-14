T = int(input())
for t in range(1,T+1):
	N = input()
	N = list(map(int,list(N)))
	s = []
	while N != s:
		for n in range(len(N)-1):
			if N[n] > N[n+1]:
				N[n+1:] = [9]*(len(N)-n-1)
				N[n]-=1
		s = sorted(N)		
	N = list(map(str,N))
	answer = ''.join(N)
	print('Case #{}: {}'.format(t,int(answer)))