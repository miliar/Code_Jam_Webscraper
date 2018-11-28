tt = int(raw_input())
for t in xrange(1, tt + 1):
	c, f, x = map(float, raw_input().split())
	cps = 2.0
	ans = x / cps
	fbs = 0
	while True:
		fbs += c / cps
		cps += f
		if fbs + x / cps < ans:
			ans = fbs + x / cps
		else:
			break
	print "Case #" + str(t) + ": " + str(ans)