t = int(raw_input())
for _ in xrange(t):
	cookies, flipper = raw_input().split()
	flipper = int(flipper)
	cookies = map(lambda x: x == '+', cookies)
	flips = 0
	for i in xrange(len(cookies) - flipper + 1):
		if not cookies[i]:
			flips += 1
			for j in xrange(i, i + flipper):
				cookies[j] = not cookies[j]
	if not all(cookies):
		result = 'IMPOSSIBLE'
	else:
		result = str(flips)
	print 'Case #%d: %s' % (_ + 1, result)