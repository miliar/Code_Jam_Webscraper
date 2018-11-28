import sys

tn = int( sys.stdin.readline().rstrip() )

for cc in xrange(tn):
	line = sys.stdin.readline().rstrip().split()

	invoke = line[-1]

	C = int( line[0] )

	combine = {} 
	oppose = ""
	opposecomb = {}
	for i in xrange(1,C+1):
		combine[ line[i][0] + line[i][1] ] = line[i][2]
		combine[ line[i][1] + line[i][0] ] = line[i][2]

	D = int( line[C+1] )
	for i in xrange(C+2,C+2+D):
		oppose += line[i]
		opposecomb[ line[i][0] + line[i][1] ] = True
		opposecomb[ line[i][1] + line[i][0] ] = True

	ret = ""
	for x in invoke:
		ret += x

		if len(ret) > 1 and combine.has_key( ret[-2:] ):
			ret = ret[:-2] + combine[ ret[-2:] ]

		ok = True
		for a in ret:
			for b in ret:
				if opposecomb.has_key(a+b):
					ret = ""
					ok = False
					break
			if not ok:
				break
	print 'Case #%d:' % (cc+1), str( list( ret ) ).replace("'","")
