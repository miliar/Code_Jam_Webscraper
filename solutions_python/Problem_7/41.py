import sys, os
from string import rstrip, split

def center(p1, p2, p3):
	(x1, y1) = p1
	(x2, y2) = p2
	(x3, y3) = p3
	print("(%d, %d)" % (x1, y1))
	print("(%d, %d)" % (x2, y2))
	print("(%d, %d)" % (x3, y3))
	xc = (float(x1) + float(x2) + float(x3)) % 3.0
	yx = (float(y1) + float(y2) + float(y3)) % 3.0
	ret = ((xc == 0.0) and (yx == 0.0))
	print ret
	return ret

# Open files to read and write
fin = open(os.getcwd() + '/' + sys.argv[1], 'r')
fout = open(os.getcwd() + '/' + sys.argv[1] + '.out', 'w')

# Process the input
numCases = int(rstrip(fin.readline(), '\n'))

for case in xrange(numCases):
	print "CASE"
	vals = split(rstrip(fin.readline(), '\n'), ' ')
	(n, A, B, C, D, x0, y0, M) = (int(vals[0]), int(vals[1]), int(vals[2]), int(vals[3]), int(vals[4]), int(vals[5]), int(vals[6]), int(vals[7]))
	

	points = []
	x = x0
	y = y0
	points.append((x,y))
	for i in xrange(1, n): #for i = 1 to n-1   CHECK THIS!!!
		x = (A * x + B) % M
		y = (C * y + D) % M
		points.append((x, y))
	print("len(points): %d" % len(points))
	goodTris = 0
	for a in xrange(len(points) - 2):
		for b in xrange(a + 1, len(points) - 1):
			for c in xrange(b + 1, len(points)):
				if center(points[a], points[b], points[c]):
					goodTris += 1
	fout.write("Case #%d: %d\n" % (case + 1, goodTris))


# Close the input file stream
fin.close()
# Close the output file stream
fout.close()
