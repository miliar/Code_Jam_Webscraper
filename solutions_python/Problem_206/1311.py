def slowest_horse(D,K,S,N):
	time_taken = list()
	for i in range(N):
		k,s = K[i],S[i]
		time_taken.append((D-k)/s)
	return D/max(time_taken)

T = int(input())

for i in range(T):
	D,N = input().split()
	D,N = int(D), int(N)
	K,S = list(),list()
	for j in range(N):
		k,s = input().split()
		K.append(int(k))
		S.append(int(s))
	string = 'case #'+str(i+1)+': '+str(slowest_horse(D,K,S,N))
	print(string)
	
