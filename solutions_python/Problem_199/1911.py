def flip(i, k):
	for x in range(i, i+k):
		s[x] = '+' if s[x] == '-' else '-'

t = int(raw_input())

for tc in xrange(t):
	s, k = raw_input().split()
	s, k = list(s), int(k)
	flips = 0
	l = len(s)
	for i in xrange(l):
		p = s[i]
		if p == '-':
			if k > l-i:
				flips = 'IMPOSSIBLE'
				break
			else:
				flips += 1
				flip(i, k)

	flips = str(flips)
	print 'Case #%d: %s' % (tc+1, flips)
