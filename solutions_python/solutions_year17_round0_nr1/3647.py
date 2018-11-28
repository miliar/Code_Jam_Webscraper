t = int(raw_input())

for t_i in range(t):
	s, k = raw_input().split()
	s = list(s)
	k = int(k)

	flips = 0
	for i in range(len(s) - k + 1):
		if (s[i] == '-'):
			for j in range(k):
				if (s[i + j] == '-'):
					s[i + j] = '+'
				else:
					s[i + j] = '-'
			flips += 1

	if (not all(c == s[0] for c in s)):
		result = 'IMPOSSIBLE'
	else:
		result = str(flips)

	print('Case #' + str(t_i + 1) + ': ' + result)
