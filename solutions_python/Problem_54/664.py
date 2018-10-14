def mcd(a, b):
	while b != 0:
		a, b = b, a - b * ( a / b )

	return a
for case in range(1, input()+1):
	t = [int(d) for d in raw_input().split(' ')[1:]]

	d = abs(t[0] - t[1])
	for i in t[2:]:
		d = mcd(d, abs(t[0]-i))

	y = ((-t[0] % d) + d ) %d

	print "Case #%d: %d" % (case, y)
