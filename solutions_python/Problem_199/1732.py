for t in range(int(input())):
	s,k = input().split()
	s = list(s)
	k = int(k)
	steps = 0
	i = 0
	def flip(i):
		f = -1
		for j in range(i, i + k):
			if s[j] == '+':
				s[j] = '-'
				if f == -1:
					f = j
			else:
				s[j] = '+'
		return f
	while i <= len(s) - k:
		if s[i] == '-':
			f = flip(i)
			steps += 1
			if f == -1:
				i += 1
			else:
				i = f
		else:
			i += 1
	if s.count('-') > 0:
		print('Case #{}: IMPOSSIBLE'.format(t + 1))
	else:
		print('Case #{}: {}'.format(t + 1,steps))