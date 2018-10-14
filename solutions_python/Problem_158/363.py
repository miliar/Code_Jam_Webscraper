import math

infile = open("D-small-attempt1.in")
outfile = open("output", "w")

ncases = int(infile.readline())

for i in xrange(0, ncases):
	x, r, c = map(int, infile.readline().strip("\n").split(" "))
	outfile.write("Case #%d: " % (i + 1))

	size = math.floor(x / 2)
	if x > 6:
		outfile.write("RICHARD")
	elif r * c % x != 0:
		outfile.write("RICHARD")
	elif x == 2:
		outfile.write("GABRIEL")
	elif r < size + 1 or c < size + 1:
		outfile.write("RICHARD")
	else:
		outfile.write("GABRIEL")

	outfile.write("\n")
