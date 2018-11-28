def dance(n, s, pmax, scores):
	solution = 0
	surprising = int(s)
	for score in scores:
		if int(score) < int(pmax):
			continue			
		if int(score) >= int(pmax)*3-2:
			solution +=1
		elif int(score) <= int(pmax)*3-5:			
			continue
		else:
			if surprising > 0:								
				solution +=1
				surprising -=1
	return solution






def get_problems():
	f = file("B-large.in")
	f2 = open("B-large.out", 'w')
	numCases = f.readline()
	for i in xrange(1, int(numCases)+1):
		line = f.readline().split()
		output = dance(line[0], line[1], line[2], line[3:] )		
		stra = "Case #%d: %s" % (i, output)
		print stra		
		f2.write(stra + "\n")

get_problems()