swap = {'-': '+', '+': '-'}
N = int(raw_input())
for i in range(N):
	S, K = raw_input().split()
	S, K = list(S), int(K)
	count = 0
	for j in range(len(S)-K+1):
		if S[j] == '-':
			for k in range(K):
				S[j+k] = swap[S[j+k]]
			count+= 1
				
	if '-' in S:
		print("Case #%d: IMPOSSIBLE" % (i+1))
	else:
		print("Case #%d: %d" % (i+1, count))
		
		