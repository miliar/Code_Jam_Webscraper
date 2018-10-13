T = int(raw_input())

for re in range(T):
	s = raw_input().split()
	s, k = list(s[0]), int(s[1])
	ans = 0
	for i in range(len(s) - k + 1):
		if s[i] == '-':
			s[i:i+k] = map(lambda x : '+' if x == '-' else '-', s[i:i+k])
			ans += 1
	if '-' in s:
		ans = 'IMPOSSIBLE'
	print 'Case #' + str(re+1) + ':', ans