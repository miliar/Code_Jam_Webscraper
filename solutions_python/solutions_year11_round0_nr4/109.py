nc = input()
for ci in range(1, nc + 1):
	n = input()
	a = [int(x) for x in raw_input().split()]
	ans = 0.0
	for i in range(0, n):
		if a[i] != i + 1:
			ans += 1
	print "Case #%d: %f" % (ci, ans)
