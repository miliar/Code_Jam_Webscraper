v = [line.strip() for line in open('a.in','r').readlines()]

v = v[1:]

#print(v)

out = open('a.out', 'w')

for case, n in enumerate(v):
	case += 1
	d = list(n)
	b = len(set(d))
	ln = len(d)
	r = d[:]
	r[0] = 1
	dig = 0
	for i in range(1, ln):
		if d[i] in d[:i]:
			r[i] = r[d.index(d[i])]
		else:
			if dig == 1:
				dig += 1
			r[i] = dig
			dig += 1
#	print(d, r)
	x = 1
	i = ln - 1
	ans = 0
	if b == 1:
		b += 1
	while i >= 0:
		ans += r[i] * x
		x *= b
		i -= 1
	print("Case #%d: %d" % (case, ans), file = out)

