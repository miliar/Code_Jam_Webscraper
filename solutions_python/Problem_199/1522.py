def change(c):
	return '-' if c == '+' else '+'
for test in range(1, int(input()) + 1):
	s, k = input().split()
	s = list(s)
	k = int(k)
	n = len(s)
	ans = 0
	for i in range(n - k + 1):
		if s[i] == '-':
			ans += 1
			for j in range(k):
				s[i + j] = change(s[i + j])
	if s.count('+') != n:
		ans = "IMPOSSIBLE"
	print("Case #%d:" % test, ans)