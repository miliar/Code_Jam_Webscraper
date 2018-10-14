def other(P):
	if P == 'O':
		return 'B'
	else:
		return 'O'

T = int(raw_input())
for i in xrange(T):
	tmp = raw_input().split()
	N = int(tmp[0])
	tmp = tmp[1:]

	t, to = (0, 0)
	x, xo = (1, 1)
	r = ''

	for j in xrange(N):
		P = tmp[j * 2]
		R = int(tmp[j * 2 + 1])

		is_other = (r != P) and r
		if is_other:
			x, xo = (xo, x)

		dist = abs(x - R)
		if is_other:
			if (t - to) >= dist:
				dist = 0
			else:
				dist -= (t - to)
			to = t
		t += dist + 1
		x = R
		r = P

	print 'Case #%i:' % (i + 1), t

