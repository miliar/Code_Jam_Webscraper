def TidyNumber(N):
	N = list(map(int,N))
	if len(N) == 1:
		return str(N[0])

	for i in range(len(N)-1,0,-1):
		dPrev = N[i-1]
		dCurr = N[i]
		if dPrev > dCurr:
			N[i-1] -= 1
			for j in range(i,len(N)):
				N[j] = 9
		
	return str(int("".join(map(str,N)),10))


T = int(input())
for t in range(1,T+1):
	N = input().strip()
	print("Case #"+str(t)+": "+TidyNumber(N))