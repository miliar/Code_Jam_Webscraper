t = input()
def flip(c):
	if c == '-':
		return '+'
	if c == '+':
		return '-'
for tt in range(1, t + 1):
	s, k = raw_input().split()
	s = list(s)
	k = int(k)
	ans = 0
	for i in range(len(s) - k + 1):
		if s[i] == '-':
			ans += 1
			for j in range(k):
				s[i + j] = flip(s[i + j])

	if s == ['+'] * len(s):
		print 'Case #%d: %d' % (tt, ans)
	else:
		print 'Case #%d: IMPOSSIBLE' % tt