T = int(input())
for t in range(1,T+1):
	S, K = input().split()
	S = list(S)
	K = int(K)
	count = 0
	for i in range(0, len(S)-K+1):
		if S[i] == '-':
			for j in range(i,i+K):
				S[j] = '+' if S[j] == '-' else '-'
			count += 1
	S = ''.join(S)
	if '-' not in S:
		print("Case #" + str(t) + ": " + str(count))
	else:
		print("Case #" + str(t) + ": IMPOSSIBLE")
