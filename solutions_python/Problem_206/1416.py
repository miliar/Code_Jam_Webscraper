T = int(raw_input())
for test in range(T):
	D, N = (int(x) for x in raw_input().split())
	horses = [
		[int(x) for x in raw_input().split()]
		for _ in range(N)
	]

	ans = None
	for s, k in horses:
		t = (D-s+0.0)/(k+0.0)
		val = (D+0.0)/(t+0.0)
		if ans is None or val < ans:
			ans = val

	print 'Case #%d: %.6f' % (test+1, ans)
