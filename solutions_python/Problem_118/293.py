a = [(1, 1), (2, 4), (3, 9)]
q = []
def f(a):
	return (a, a ** 2)
def rek(l, i, s):
	if s > 9:
		return
	if i > (l - 1) / 2:
		for j in range(i, l):
			q[j] = q[l - 1 - j]
		t = int(''.join(q))
		a.append(f(t))
	else:
		q[i] = '0'
		rek(l, i + 1, s)
		q[i] = '1'
		rek(l, i + 1, s + (1 if i == l - 1 - i else 2))
		if i == l - 1 - i:
			q[i] = '2'
			rek(l, i + 1, s + 4)
for l in range(2, 50):
	q = ['0'] * l
	q[0] = '1'
	rek(l, 1, 2)
	a.append(f(int('2' + '0' * (l - 2) + '2')))
	if l % 2 == 1:
		a.append(f(int('2' + '0' * ((l - 2) / 2) + '1' + '0' * ((l - 2) / 2) + '2')))
for t in xrange(1, int(raw_input()) + 1):
	print "Case #" + str(t) + ":",
	b, e = map(int, raw_input().split())
	res = 0
	for (x, y) in a:
		if y > e:
			break
		if y >= b:
			res += 1
	print res