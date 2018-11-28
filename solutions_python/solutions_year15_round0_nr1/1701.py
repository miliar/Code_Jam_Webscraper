t = int(raw_input())
for i in xrange(t):
	s = raw_input().split()
	smx = int(s[0])
	num = 0
	ans = 0
	for j in xrange(smx+1):
		x = ord(s[1][j]) - 48
		if x > 0 and num < j:
			ans += j - num
			num = j
		num += x
	print 'Case #%d: %d' % (i+1, ans)
