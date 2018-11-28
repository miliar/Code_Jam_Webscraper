def can_win(n, m, p):
	if n <= p: return True
	if m == n - 1: return False
	return can_win(n / 2, m / 2 + m % 2, p)

def can_lose(n, m, p):
	if p <= 0: return True
	if n <= p: return False
	if m == 0: return False
	return can_lose(n / 2, m / 2 - (1 - m % 2), p - n / 2)
		

def solve():
	n, p = map(int, raw_input().split())
	l, r = 0, 2 ** n
	while l + 1 < r:
		m = (l + r) / 2
		if can_win(2 ** n, m, p):
			l = m
		else:
			r = m
	best_win = l
	l, r = 0, 2 ** n
	while l + 1 < r:
		m = (l + r) / 2
		if not can_lose(2 ** n, m, p):
			l = m
		else:
			r = m
	return "%d %d" % (l, best_win)

for i in xrange(input()):
	print "Case #%d: %s" % (i + 1, solve())
