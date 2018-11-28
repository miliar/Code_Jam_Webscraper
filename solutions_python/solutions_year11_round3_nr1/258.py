fileName = "A-large"
fin = open(fileName + ".in", "r")
fout = open(fileName + ".out", "w")

T = int(fin.readline())

for caseID in xrange(1, T+1):
	R, C = map(int, fin.readline().split())
	pic = []
	for i in xrange(R):
		pic.append(map(lambda x: x, fin.readline().strip()))
		#print pic[i]
	for i in xrange(R):
		for j in xrange(C):
			if pic[i][j] == "#":
				if j + 1 < C:
					if i + 1 < R:
						if pic[i][j+1] == "#":
							if pic[i+1][j] == "#":
								if pic[i+1][j+1] == "#":
									pic[i][j] = "/"
									pic[i][j+1] = "\\"
									pic[i+1][j] = "\\"
									pic[i+1][j+1] = "/"
	cp = set()
	for i in xrange(R):
		for j in xrange(C):
			cp.add(pic[i][j])
	print "Case #%d:" % caseID
	fout.write("Case #%d:\n" % caseID)	
	if "#" in cp:
		print "Impossible"
		fout.write("Impossible\n")
	else:
		for i in xrange(R):
			print "".join(pic[i])
			fout.write("".join(pic[i]) + "\n")

fin.close()
fout.close()
