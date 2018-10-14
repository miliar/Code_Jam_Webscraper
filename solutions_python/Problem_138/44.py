def f(n, a, b):
	ans = 0
	i, j = 0, 0
	while j < n:
		if a[i] < b[j]:
			i += 1
			j += 1
		else:
			j += 1
			ans += 1
	return ans

tt = int(raw_input())
for t in xrange(1, tt + 1):
	n = int(raw_input())
	a = sorted(map(float, raw_input().split()))
	b = sorted(map(float, raw_input().split()))
	print "Case #" + str(t) + ": " + str(n - f(n, b, a)) + " " + str(f(n, a, b))
