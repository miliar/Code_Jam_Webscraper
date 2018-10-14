import sys

lines = open(sys.argv[1], "rb").read().splitlines()

i = 1
case = 0
res = ""
while i < len(lines):
	case += 1
	n, q = map(int, lines[i].split())
	i += 1
	hh = []
	for j in xrange(n - 1):
		e, s = map(int, lines[i + j].split())
		hh.append([e, s])
	i += n
	dd = []
	for j in xrange(n - 1):
		d = map(int, lines[i + j].split())
		dd.append(d[j + 1])
	i += n + 1
	cur = []
	min_t = 0
	for j in xrange(n - 1):
		cur.append(hh[j] + [min_t])
		bad = []
		for idx, h in enumerate(cur):
			if h[0] < dd[j]:
				bad.append(idx)
				continue
			h[0] -= dd[j]
			h[2] += dd[j] / float(h[1])
		for idx in reversed(bad):
			cur.pop(idx)
		min_t = min([h[2] for h in cur])

	res += "Case #%d: %.9f\n" % (case, min_t)

open(sys.argv[2], "wb").write(res)
