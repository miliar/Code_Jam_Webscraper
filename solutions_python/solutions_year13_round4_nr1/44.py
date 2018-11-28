def solve():
	n, m = map(int, raw_input().split())
	events = []
	cards = []
	res = 0
	fare = lambda k: k * (n + n - k + 1) / 2
	for i in xrange(m):
		o, e, p = map(int, raw_input().split())
		events.append((o, -p))
		events.append((e, p))
		res += p * fare(e - o)
	events.sort()
	for s, p in events:
		if p < 0:
			cards.append([s, -p])
			continue
		for i in xrange(len(cards) - 1, -1, -1):
			card = cards[i]
			if (card[1] == 0): continue
			p2 = min(card[1], p)
			res -= p2 * fare(s - card[0])
			card[1] -= p2
			p -= p2
			if p == 0: break
	return res

for i in xrange(input()):
	print "Case #%d: %d" % (i + 1, solve())
