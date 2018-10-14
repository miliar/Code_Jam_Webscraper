
f = open("B-large.in", 'r')
w = open("large.txt", 'w')
cnt = 0
for line in f:
	params = line.split()
	if len(params) < 3:
		continue;
	print params

	cnt = cnt + 1
	C = float(params[0])
	F = float(params[1])
	X = float(params[2])

	curCookie = 0;
	t = 0;
	e = 2;
	while curCookie < X:
		t = t + C/e;

		if (X/(e+F)) < ((X-C)/e):
			curCookie = 0;
			e = e + F;
		else:
			t = t + (X-C)/e
			curCookie = X

	print >> w, "Case #" + str(cnt) + ": "  + str(t)
	# print "Case #", cnt, ":", t 

f.close()
w.close()	