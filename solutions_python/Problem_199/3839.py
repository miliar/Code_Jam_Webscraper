import numpy as np

t = int(input())

for test in range(t):
	s, k = input().split()
	k = int(k)
	s = np.array([1 if c=='+' else 0 for c in s])

	cnt = 0
	bad = False
	for ix in range(len(s)):
		if s[ix] == 1:
			continue
		else:
			#print(ix)
			if ix + k <= len(s):
				s[ix:ix+k] = 1 - s[ix:ix+k]
				cnt += 1
				#print(s)
			else:
				bad = True

	print('Case #{}: {}'.format(test+1, 'IMPOSSIBLE' if bad else str(cnt)))
