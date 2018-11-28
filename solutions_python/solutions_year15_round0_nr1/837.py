T = int(raw_input())

for case in xrange(1, T + 1):
	sm, sl = raw_input().split()

	prev = 0
	ans = 0
	for i in xrange(len(sl)):
		if prev < i:
			ans += i - prev
			prev += i - prev
		prev += int(sl[i])

	print 'Case #%d: %d' % (case, ans)