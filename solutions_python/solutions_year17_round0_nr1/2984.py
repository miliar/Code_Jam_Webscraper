def flip(x):
	if x == '+':
		return '-'
	return '+'

T = int(input())
for tc in range(1, T+1):
	s, k = input().split()
	s = list(s)
	k = int(k)
	l = len(s)
	c = 0
	for i in range(l-k+1):
		if s[i] == '-':
			for j in range(i, i+k):
				s[j] = flip(s[j])
			c = c+1
	if '-' in s:
		c = 'IMPOSSIBLE'
	else:
		c = str(c)
	print('Case #{0}: {1}'.format(str(tc),str(c)) )


