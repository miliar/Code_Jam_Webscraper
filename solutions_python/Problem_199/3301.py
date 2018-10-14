#!/usr/bin/python


m = map(lambda i: 1 << i, xrange(10))

def solve(b, n, k):
	t = (1 << n) - 1
	if t == b:
		return 0
	queue = [b]
	steps = [0]
	qi = 0
	while qi < len(queue):
		b = queue[qi]
		for p in xrange(n - k + 1):
			newbie = reduce(lambda r, i: r ^ m[p + i], xrange(k), b)
			if newbie not in queue:
				if newbie == t:
					return steps[qi] + 1
				queue.append(newbie)
				steps.append(steps[qi] + 1)
		qi += 1
	return 'IMPOSSIBLE'


for t in xrange(1, int(raw_input()) + 1):
	s, k = raw_input().split()
	n = len(s)
	b = reduce(lambda r, (i, c): r | (m[i] if c == '+' else 0), enumerate(s), 0)
	result = solve(b, n, int(k))
	print "Case #{}: {}".format(t, result)
