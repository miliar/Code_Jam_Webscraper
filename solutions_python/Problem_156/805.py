def cost(n, val):
	if n<=val:
		return 0
	ret = 10000;
	for i in xrange(1, n):
		p1 = i
		p2 = n - p1
		ret = min(ret, 1+cost(p1, val)+cost(p2, val))
	return ret

t = int(raw_input())
for i in xrange(t):
	n = int(raw_input())
	arr = map(int, raw_input().split())
	mx = 0
	ans = 0
	fi = 10000
	for val in xrange(2,1000):
		ans = 0
		for j in xrange(n):
			ans += cost(arr[j], val)
			mx = max(mx, arr[j])

		ans += min(val, mx)
		ans = min(ans, mx)
		fi = min(ans, fi);
	
	print "Case #"+str(i+1)+": "+str(fi)
