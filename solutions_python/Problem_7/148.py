import sys

if len(sys.argv) != 3 :
	print "Usage: python %s inputfile outputfile" % (sys.argv[0])
	sys.exit(1)

infile = sys.argv[1]
inp = open(infile)
outfile = sys.argv[2]
outp = open(outfile, "w")



num_cases = int(inp.readline())
i = 1
while i <= num_cases:
	count = 0
	n, A, B, C, D, x_0, y_0, M = [int(x) for x in inp.readline().strip().split()]
	vertices = []
	X = x_0
	Y = y_0
	vertices.append((X,Y))
	for j in range(1,n) :
		X = (A*X+B) % M
		Y = (C*Y+D) % M
		vertices.append((X,Y))

	triangles = []
	for r in range(0, len(vertices)) :
		for s in range(r+1, len(vertices)) :
			for t in range(s+1, len(vertices)) :
				a = vertices[r]
				b = vertices[s]
				c = vertices[t]
				triangles.append(set([a,b,c]))

	for tri in triangles :
		(a0,a1), (b0,b1), (c0,c1) = tri
		if ((a0+b0+c0) % 3 == 0) and ((a1+b1+c1) % 3 == 0) :
			count += 1		
	
	line = "Case #" + str(i) + ": " + str(count)
	outp.write(line + '\n')
	i += 1

inp.close()
outp.close()
