T = int(raw_input().strip())
for i in range(1,T+1):
	S, K = raw_input().strip().split()
	K = int(K)
	S = list(S)

	# Algorithm sketch, go left to right
	ans = 0
	for j in range(len(S)-K+1):
		if S[j] == '-':
			ans += 1
			for k in range(K):
				if S[j+k] == '-':
					S[j+k] = '+'
				else:
					S[j+k] = '-'
	# Check Answer	
	for s in S:
		if s == '-':
			ans = 'IMPOSSIBLE'

	print 'Case #{0}: {1}'.format(i, ans)