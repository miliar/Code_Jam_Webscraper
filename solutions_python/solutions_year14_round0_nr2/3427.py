T = int(raw_input())
for i in range(1, T+1):
	C, F, X = map(float, raw_input().split())
	ans = []
	ans.append(X/2)
	ans.append(C/2 + X/(2+F))
	k = 1
	while ans[k] < ans[k-1]:
		k += 1
		rate = 2 + k * F
		s = 0
		for j in range(k):
			s += C/(2 + j * F)
		s += X / rate
		ans.append(s)
	print "Case #%s: %0.7f" % (i, ans[k-1])