t = input()
for tt in range(1, t + 1):
	n, k = map(int, raw_input().split())
	k -= 1
	for b in range(100):
		if 2 ** (b + 1) - 1 > k:
			break
	x = k - ((2 ** b) - 1)
	n -= (2 ** b) - 1
	ans = n / 2 ** b
	if x < n % 2 ** b:
		ans += 1
	print 'Case #%d: %d %d' % (tt, ans / 2, (ans - 1) / 2)
