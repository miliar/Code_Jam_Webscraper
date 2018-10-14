for test in range(1, int(input()) + 1):
	d, n = map(int, input().split())
	tm = 0
	for i in range(n):
		k, s = map(int, input().split())
		tm = max(tm, (d - k) / s)
	ans = d / tm
	print("Case #%d: %.6f" % (test, ans))
