t = input()
tc = 1
while t:
	t -= 1
	s = raw_input().split()
	k = int(s[1])
	s = s[0]
	n = len(s)
	ss = []
	for i in s:
		if i == '-':
			ss.append(0)
		else:
			ss.append(1)
	s = ss[:]
	i = 0
	ans = 0
	while i <= n - k:
		if s[i] == 0:
			ans += 1
			c = 0
			while c < k:
				s[i + c] = 1 - s[i + c]
				c += 1
		i += 1
	if sum(s) == n:
		print "Case #{0}: {1}".format(tc, ans)
	else:
		print "Case #{0}: IMPOSSIBLE".format(tc)
	tc += 1