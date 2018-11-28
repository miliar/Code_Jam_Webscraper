T = int(raw_input())
for t in xrange(T):
	N = int(raw_input())
	S = 0
	mat = [raw_input() for i in xrange(N)]
	last1 = []
	for r in xrange(N):
		l = 0
		for c in xrange(N-1, -1, -1):
			if (mat[r][c]=='1'):
				l = c
				break
		last1.append(l)
	for r1 in xrange(N):
		if last1[r1]>r1:
			r2 = r1+1
			while (last1[r2]>r1): r2+=1
			#print mat
			mat.insert(r1, mat.pop(r2))
			last1.insert(r1, last1.pop(r2))
			#print mat
			S+=r2-r1
			#print "Swap %d %d" % (r1, r2)
	print 'Case #%d: %d' % (t+1, S)
	#print last1
	
