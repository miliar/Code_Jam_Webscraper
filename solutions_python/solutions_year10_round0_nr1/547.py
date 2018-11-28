def light(n, k):
	s = 2 ** n - 1
	if k == 0 or k < s: return False
	return (k - s) % (s + 1) == 0

T = int(raw_input())
for case in xrange(1, T + 1):
	N, K = [int(i) for i in raw_input().split()]
	print "Case #%d: %s" % (case, 'ON' if light(N, K) else 'OFF')
