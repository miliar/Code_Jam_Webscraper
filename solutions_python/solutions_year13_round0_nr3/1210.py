import math

def fuck(s, S):
	if s == 0:
		return 0
	if s == 1:
		if S == 1:
			return 1
		return 0
	if s == 10:
		if S == 11:
			return 1
		return 0
	if s + 1 <= S:
		return 2 * fuck(s / 100, (S - s) / 10)
	if s <= S:
		return fuck(s / 100, (S - s) / 10)
	return fuck(s / 100, S / 10)

def count(S):
	n = 0
	if 1 <= S:
		n += 1
	if 2 <= S:
		n += 1
	if 3 <= S:
		n += 1
	k, s = 2, 10
	while s * 10 < S:
		if k % 2 == 0:
			n += 2
			d = (k - 2) / 2
			if k >= 4:
				n += d
			if k >= 6:
				n += d * (d - 1) / 2
			if k >= 8:
				n += d * (d - 1) * (d - 2) / 6
		else:
			n += 3
			d = (k-3)/2
			if k >= 5:
				n += 2 * d
			if k >= 7:
				n += d * (d - 1)
			if k >= 9:
				n += d * (d - 1) * (d - 2) / 3
		s *= 10
		k += 1
	s += 1
	if s <= S:
		n += 1
		if k % 2 == 0:
			if s * 2 <= S:
				n += 1
		else:
			d = 10 ** ((k - 1) / 2)
			if s + 2 * d <= S:
				n += 1
			if s * 2 + d <= S:
				n += 1
		n += fuck(s / 100, (S - s) / 10)
	return n

T = int(raw_input())

for t in range(1, T + 1):
	p = raw_input().split(' ')
	A, B = int(p[0]), int(p[1])
	#print A, B
	A = int(math.ceil(A ** 0.5))
	B = int(math.floor(B ** 0.5))
	#print A, B
	ca = count(A)
	cb = count(B)
	#print ca, cb
	d = cb - ca
	if count(A - 1) < ca:
		d += 1
	print 'Case #%d: %d' % (t, d)
	#print ''
