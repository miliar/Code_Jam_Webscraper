n = input()
for _ in xrange(n):
	d = input()
	p = map(int,raw_input().split())
	p.sort(reverse=True)
	p_max = p[0]
	ans = p_max
	# check ans if make all value <= k
	for k in xrange(1,p_max):
		special_minutes = 0
		for v in p:
			if v <= k:
				break
			special_minutes += v / k
			if v % k == 0:
				special_minutes -= 1
		if ans > k + special_minutes:
			ans = k + special_minutes

	print "Case #%d: %d" % (_+1,ans)