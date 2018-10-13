f = open('D-small-attempt1.in')
o = open('output.dat', 'w')

N = int(f.readline())

for i in range(N):
	x, r, c = map(int, f.readline().strip().split())

	if x == 1:
		winner = 'GABRIEL'

	if x == 2:
		if (r * c) % 2 == 0:
			winner = 'GABRIEL'
		else:
			winner = 'RICHARD'

	if x == 3:
		if (r * c) % x == 0 and (c > 1 and r > 1):
			winner = 'GABRIEL'
		else:
			winner = 'RICHARD'

	if x == 4:
		if (r * c) % x == 0 and (c > 2 and r > 2):
			winner = 'GABRIEL'
		else:
			winner = 'RICHARD'

	# print >>o, x, r, c
	print >>o, "Case #" + str(i + 1) + ": " + winner