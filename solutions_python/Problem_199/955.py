T = input()

for i in range(T):
	S, K = raw_input().split()
	K = int(K)
	count = 0
	L = len(S)
	for j in range(L - K + 1):
		if S[j] == '+':
			continue
		count += 1
		S = S[ : j] + ''.join([('+', '-')[S[k] == '+'] for k in range(j, j + K)]) + S[j + K : ]

	print 'Case #%s:' % (i + 1),
	if '-' in S[L - K + 1 : ]:
		print 'IMPOSSIBLE'
	else:
		print count