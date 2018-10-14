for t in range(int(input())):
	d, n = (int(i) for i in input().split())
	tm = 0
	for i in range(n):
		k, s = (int(i) for i in input().split())
		r = (d - k) / s
		if r > tm:
			tm = r
	print("Case #%d: %.6f" % (t + 1, d / tm))