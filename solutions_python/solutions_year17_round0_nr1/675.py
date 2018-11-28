T=int(input())
for t in range(T):
	c = 0
	L=[x for x in raw_input().split()]
	K=int(L[1])
	S=list(L[0])
	for i in range(0,len(S)):
		if S[i]=='-':
			if len(S)-i < K:
				c = -1
				break
			c += 1
			for j in range(i, i+K):
				if S[j] == '-':
					S[j] = '+'
				else:
					S[j] = '-'
	if c == -1:
		print("Case #%d: IMPOSSIBLE"%(t+1))
	else:
		print("Case #%d: %d"%(t+1,c))
