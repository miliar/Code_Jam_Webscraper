t = int(input())
for z in range(t):
	s, k = input().split()
	k = int(k)
	s = list(s)
	flips = 0
	
	for i in range(len(s) - k + 1):
		if s[i] == '-':
			flips += 1
			for j in range(i, i + k):
				s[j] = '+' if s[j] == '-' else '-'

	ok = True
	for c in s:
		if c == '-':
			ok = False
	
	print('Case #{0}: {1}'.format(z + 1, flips if ok else 'IMPOSSIBLE'))
