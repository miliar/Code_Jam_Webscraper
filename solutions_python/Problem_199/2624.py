T = int(raw_input())
for tc in range(1, T+1):
	s, m = raw_input().split()
	m = int(m)
	n = len(s)
	s = list(s)
	action = 0
	for i in range(n - m + 1):
		if s[i] == '-':
			action += 1
			for j in range(i, i + m):
				s[j] = '+' if s[j] == '-' else '-'
	print 'Case', '#' + str(tc) + ':', 
	if all(map(lambda p:p == '+', s)):
		print action
	else:
		print 'IMPOSSIBLE'

