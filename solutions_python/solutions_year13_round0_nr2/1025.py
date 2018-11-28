n = int( raw_input().strip() )

for i in xrange(n) :
	N, M = map( int, raw_input().split(" ") )
	lawn = [0] * N
	for k in xrange(N) :
		lawn[k] = map( int, raw_input().split(" ") )

	maxN = [0] * N
	maxM = [0] * M
	for k in xrange(N) :
		maxN[k] = max(lawn[k])
	for k in xrange(M) :
		maxM[k] = max(map(list, zip(*lawn))[k])

	flag = True
	for x in xrange(N) :
		for y in xrange(M) :
			if lawn[x][y] < maxN[x] and lawn[x][y] < maxM[y] :
				flag = False
				break
	if flag :
		print "Case #" + str(i+1) + ": YES"
	else :
		print "Case #" + str(i+1) + ": NO"