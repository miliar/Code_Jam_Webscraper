def bath_stalls(N,K):
	twoth = 0
	for i in range(61):
		if K<pow2[i]:
			twoth = pow2[i]
			break
	nrem = N-twoth+1
	val1 = nrem//twoth
	srem = twoth - nrem % twoth
	lrem = nrem % twoth
	if lrem == srem:
		return(str(val1+1),str(val1))
	elif lrem>srem:
		if twoth-srem <= K:
			return(str(val1+1),str(val1))
		else:
			return(str(val1+1),str(val1+1))
	else:
		if pow2[i-1] <= K< pow2[i-1]+lrem:
			return(str(val1+1),str(val1))
		else:
			return(str(val1),str(val1))
			 
	

T = int(input())
pow2 = list()
pow2.append(1)
for i in range(1,61):
	pow2.append(2*pow2[-1])

for i in range(T):
	N, K = input().split()
	N, K = int(N), int(K)
	print('Case #'+str(i+1)+': '+str(' '.join(list(bath_stalls(N,K)))))
