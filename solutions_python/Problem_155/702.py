from sys import exit
T = input()
for z in xrange(T):
	n, b = raw_input().split()
	n = int(n) + 1
	a = [int(b[i]) for i in range(n)]
	s = 0
	ans = 0
	for i in range(n):
		if s < i:
			ans = ans + i - s
			s = i
		s = s + a[i]
	print 'Case #%d: %d' % (z+1, ans)



