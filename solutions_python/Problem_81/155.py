from sys import stdin

t = int(stdin.readline())

for tc in xrange(t):
	n = int(stdin.readline())

	table = []
	wp = []
	owp = []
	oowp = []
	for j in xrange(n):
		table.append(stdin.readline().strip())
	
	for i in xrange(n):
		w = 0
		total = 0
		for c in table[i]:
			if c != ".":
				total += 1
			if c == "1":
				w += 1
		wp.append((w,total))
	
	for i in xrange(n):
		r = 0;
		for j in xrange(n):
			if table[i][j] != ".":
				r += float(wp[j][0]-1+int(table[i][j])) / (wp[j][1]-1)
		owp.append(r/wp[i][1])
	
	for i in xrange(n):
		r = 0;
		for j in xrange(n):
			if table[i][j] != ".":
				r += owp[j]
		oowp.append(r/wp[i][1])

	print "Case #%d:" % (tc+1)

	for i in xrange(n):
		print "%.10lf" % (0.25 * float(wp[i][0])/wp[i][1] + 0.5 * owp[i] + 0.25 * oowp[i])

