t = int(raw_input())

cost = lambda dist, n: (dist * n - (dist - 1)*dist / 2) % MOD
MOD = 10**9 + 2013

def solve():
	n, m = map(int, raw_input().split())
	inp = [tuple(map(int, raw_input().split())) for i in xrange(m)]
	ev = []
	for o, e, p in inp:
		ev.append((o, 'e', p))
		ev.append((e, 'x', p))
	ev.sort()
	naive = 0
	for o, e, p in inp:
		naive += p * cost(e - o, n)
	naive %= MOD
	oth = 0
	stack = []
	for c, t, ct in ev:
		if t == 'e':
			stack.append((c, ct))
		else:
			while ct > 0:
				origin, ctx = stack.pop()
				am = min(ct, ctx)
				if ctx > ct:
					stack.append((origin, ctx - ct))
				ct -= am
				oth += am * cost(c - origin, n)
				oth %= MOD
	return (naive - oth + MOD) % MOD

for t in xrange(1, t+1):
	print 'Case #%d:' % t,
	print solve()
