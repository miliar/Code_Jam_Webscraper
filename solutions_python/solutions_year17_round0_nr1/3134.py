T=int(input().strip())

for case in range(0, T):
	S,K=str(input().strip()).split(' ')
	K = int(K)
	S = list(S)
	
	flips = 0
	while '-' in S:
		i = S.index('-')
		if i > len(S) - K:
			break
		flips += 1
		for k in range(i, i+K):
			S[k] = '+' if S[k] == '-' else '-'

	if '-' in S:
		print("Case #" + str(case+1) + ": IMPOSSIBLE")
	else:
		print("Case #" + str(case+1) + ": " +str(flips))
