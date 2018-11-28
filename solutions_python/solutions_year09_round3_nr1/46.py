n = int(input())

for tc in range(1, n + 1):
	s = input()
	base = len(set(s))
	if base == 1:
		print("Case #%d: %d" % (tc, 2**len(s) - 1))
		continue
	m = {}
	for i in range(len(s)):
		c = s[len(s) - i - 1]
		if not c in m:
			m[c] = 0
		m[c] += base**i
	#print(m)
	digs = list(m.items())
	digs.sort(key = lambda p: -p[1])
	si = 0
	for i, d in enumerate(digs):
		if s[0] != d[0]:
			digs.pop(i)
			si += 1
			break
	#print(digs)
	res = 0
	for i, (c, dig) in zip(range(si, si + len(digs)), digs):
		res += i*dig
	print("Case #%d: %d" % (tc, res))
	