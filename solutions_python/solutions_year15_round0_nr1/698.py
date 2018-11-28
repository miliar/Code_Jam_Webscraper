T = int(raw_input())
for kase in range(1, T + 1):
	_, m = raw_input().split()
	m = map(int, list(m))
	n = len(m) - 1
	cur = m[0]
	ans = 0
	for req in range(1, n + 1):
		if cur < req:
			ans += req - cur
			cur = req
		cur += m[req]
	
	print "Case #" + str(kase) + ": " + str(ans)
