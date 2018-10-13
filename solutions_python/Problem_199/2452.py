import numpy as np


def f(c):
	return 1 if c == '+' else -1

T = int(raw_input())
for i in range(T):
	S, K = raw_input().split()
	S = np.array([f(c) for c in S]) 
	K = int(K)
	n = 0
	while True:
		a = np.where(S < 0)[0]
		if len(a) == 0:
			print('case #{}: {}'.format(i+1, n))
			break
		else:
			if a[0] + K > len(S):
				print('case #{}: IMPOSSIBLE'.format(i+1))
				break
			else:
				S[a[0]:a[0]+K] *= -1
				n += 1
