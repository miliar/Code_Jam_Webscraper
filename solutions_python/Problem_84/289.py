for casenum in xrange(1,1+int(raw_input())):
	[R, C] = [int(z) for z in raw_input().split()]
	pic = []
	for i in xrange(R):
		pic.append(raw_input())
	ans = ''
	for i in xrange(R - 1):
		for j in xrange(C - 1):
			if pic[i][j] == '#':
				if pic [i+1][j] == '#' and pic[i][j+1] == '#' and pic[i+1][j+1] == '#':
					st1 = pic[i][:j] + '/\\' + pic[i][j+2:]
					st2 = pic[i+1][:j] + '\\/' + pic[i+1][j+2:]
					pic[i] = st1
					pic[i+1] = st2
	for i in xrange(R):
		for j in xrange(C):
			if pic[i][j] == '#':
				ans = 'Impossible'
	if ans != 'Impossible':
		print ("Case #%d: " % casenum)
		for i in xrange(R):
			print pic[i]
	else:
		print ("Case #%d: " % casenum)
		print (ans)