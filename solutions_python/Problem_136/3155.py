T = int(raw_input())
for n in range(T):
	C,F,X = [float(i) for i in raw_input().split()]
	r = 2.0
	a = 0.0
	while True:
		t1 = X/r
		t2 = X/(r+F) + C/r
		if t2 < t1:
			a += C/r
			r += F
		else:
			a += X/r
			break
	print "Case #%d: %.8f" % (n+1, a)
