#!/usr/bin/env python3
T = int(input())
for kase in range(1, T + 1):
	S, K = input().split()
	K = int(K)
	ans = 0
	for i in range(len(S) - K + 1):
		if S[i] == '-':
			ans += 1
			for j in range(K):
				if S[i + j] == '-':
					S = S[ : i + j] + '+' + S[i + j + 1 : ]
				else:
					S = S[ : i + j] + '-' + S[i + j + 1 : ]
	res = ans
	if S != '+' * len(S):
		res = 'IMPOSSIBLE'
	print('Case #%d:' % kase, res)
