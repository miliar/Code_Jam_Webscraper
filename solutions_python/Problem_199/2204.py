t = int(input())
for i in range(t):
	ans = 0
	line = input()
	s, k = line.split()
	k = int(k)
	s = list(s)
	n = len(s)
	for j in range(n - k + 1):
		if s[j] == '+':
			continue
		for l in range(j, j + k):
			s[l] = '-' if s[l] == '+' else '+'
		ans += 1
	for ch in s:
		if ch != '+':
			ans = 'IMPOSSIBLE'
			break
	print('Case #%d:' % (i + 1), ans)