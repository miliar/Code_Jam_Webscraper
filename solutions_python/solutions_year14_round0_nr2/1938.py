T = int(raw_input())
for i in range(T):
	C, F, X = map(float, raw_input().split())
	j = 0
	r = 2.0
	ans = 0.0
	while True:
		T1 = X / (r + j * F)
		T2 = C / (r + j * F) + X / (r + (j+1) * F)
		if T1 <= T2:
			ans += T1
			break
		else:
			ans += C / (r + j * F)
		j = j + 1
	print "Case #%d: %.8f" % (i+1,ans)