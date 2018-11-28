qq = [0, 0, 0, 1, 2, 2, 3]
t = int(raw_input())
for i in xrange(t):
	[x, r, c] = map(int, raw_input().split())
	if r < c:
		r, c = c, r
	if x > 6 or r*c%x!=0 or x > r or c <= qq[x] or (x == 5 and c == 3):
		print 'Case #%d: RICHARD' % (i+1)
	else:
		print 'Case #%d: GABRIEL' % (i+1)
