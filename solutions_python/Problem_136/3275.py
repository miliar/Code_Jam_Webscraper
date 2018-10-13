n = int(raw_input())

for i in range(1, 1 + n):
	c, f, x = map(float, raw_input().split())
	cps = 2.0

	t = 0.0
	at = 0.0

	if c >= x:	
		print "Case #%d: %.7f" % (i, x/cps)
		continue

	while True:
		at += c
		t += c/cps

		end = (x - at)/cps

		if end > (x - (at - c))/(cps + f):
			cps += f
			at -= c
		else:
			t += end
			break

	print "Case #%d: %.7f" % (i, t)