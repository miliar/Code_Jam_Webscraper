def cycle(n, begin):
	i = begin
	while i < n + begin:
		yield i % n
		i += 1

def money(g, b, cap):
	c = cycle(len(g), b)
	sum = 0
	for i in c:
		sum += g[i]
		if sum == cap:
			try:
				j = c.next()
			except StopIteration:
				j = b
			return sum, j
		elif sum > cap: return sum - g[i], i
	return sum, b

T = int(raw_input())
for case in xrange(1, T + 1):
	R, k, N = [int(i) for i in raw_input().split()]
	group = [int(i) for i in raw_input().split()]

	ans = 0
	b = 0
	for r in xrange(R):
		sum, b = money(group, b, k)
		ans += sum
	print "Case #%d: %d" % (case, ans)
