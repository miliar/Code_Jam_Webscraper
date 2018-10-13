inp = open("D-small-attempt0.in", "r")
R=lambda:map(int, inp.readline().strip().split(' '))

outp = open("output.txt", "w")

T, = R()
for c in xrange(1, T + 1):
	outp.write('Case #%d: ' % c)
	x,r,c, = R()
	if (r < c) :
		t = r
		r = c
		c = t

	if (r * c) % x != 0:
		outp.write('RICHARD\n')
	elif x == 1 or x == 2:
		outp.write('GABRIEL\n')
	elif x == 3:
		if r < 3 or c < 2:
			outp.write('RICHARD\n')
		else:
			outp.write('GABRIEL\n')
	elif x == 4:
		if r < 4 or c < 3:
			outp.write('RICHARD\n')
		else:
			outp.write('GABRIEL\n')