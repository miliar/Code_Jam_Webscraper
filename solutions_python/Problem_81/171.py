fileName = "A-large"
fin = open(fileName + ".in", "r")
fout = open(fileName + ".out", "w")

T = int(fin.readline())

for caseID in xrange(1, T+1):
	N = int(fin.readline())
	table = dict()
	for i in xrange(N):
		temp = fin.readline().strip()
		for j in xrange(len(temp)):
			if (i, j) not in table:
				if temp[j] == '.':
					table[(i, j)] = -1
				else:
					table[(i, j)] = int(temp[j])
	WP = dict()
	for i in xrange(N):
		win = 0
		lose = 0
		for j in xrange(N):
			if table[(i, j)] == 0:
				lose += 1
			elif table[(i, j)] == 1:
				win += 1
		WP[i] = win / float(win + lose)
		#print WP[i]
	
	OWP = dict()
	for i in xrange(N):
		count = 0
		total = 0
		for j in xrange(N):
			if table[(i, j)] >= 0:
				count += 1
				win = 0
				lose = 0
				for k in xrange(N):
					if k != i:
						if table[(j, k)] == 0:
							lose += 1
						elif table[(j, k)] == 1:
							win += 1
				total += (win / float(win + lose))
		OWP[i] = total / float(count)
		#print OWP[i]
	
	OOWP = dict()
	for i in xrange(N):
		count = 0
		total = 0
		for j in xrange(N):
			if table[(i, j)] >= 0:
				count += 1
				total += OWP[j]
		OOWP[i] = total / float(count)
		#print OOWP[i]
	
	RPI = dict()
	for i in xrange(N):
		RPI[i] = WP[i] / float(4) + OWP[i] / float(2) + OOWP[i] / float(4)
		#print RPI[i]
	
	print "Case #%d:" % caseID
	fout.write("Case #%d:\n" % caseID)
	for i in xrange(N):
		print RPI[i]
		fout.write(str(RPI[i]))
		fout.write("\n")
	

fin.close()
fout.close()
