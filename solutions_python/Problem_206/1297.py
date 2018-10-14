import sys

def solve(d, others):
	return d / max([(d-h[0]) / h[1] for h in others])

with open(sys.argv[1]) as fd:
	lines = fd.readlines()
	t = int(lines.pop(0).strip())
	i = 0
	while t > i:
		i += 1
		d, n = map(int, lines.pop(0).strip().split())
		others = []
		while n:
			n -= 1
			h = map(float, lines.pop(0).strip().split())
			others.append(h)
		print "Case #%d: %0.6f" % (i, solve(float(d), others))
