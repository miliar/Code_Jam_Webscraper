v = [l.strip() for l in open('A.in').readlines()]

nt = int(v[0])
v = v[1:]

for t in range(1, nt + 1):
	n = int(v[0])
	m = [0] * n
	for i, s in enumerate(v[1:n+1]):
		ix = n - 1
		while ix >= 0 and s[ix] == '0':
			ix -= 1
			m[i] += 1
#	print(m, v[1:n+1])
	v = v[n + 1:]
	lim, ix = n - 1, 0
	cnt = 0
	while ix < n:
		fnd = ix
		while m[fnd] < lim: fnd += 1
		cnt += fnd - ix
		el = m.pop(fnd)
		m.insert(ix, el)
		lim -= 1
		ix += 1
	print('Case #%d: %d' % (t, cnt))

