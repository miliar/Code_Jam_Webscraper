caseCount = int(raw_input())

cost = 0
factor = 0
target = 0

def getOptimal(time, production):
	t = target/production
	m = cost/production + target/(production+factor)
	while t > m:
		time += cost/production
		production += factor
		t = time + target/production
		m = time + cost/production + target/(production+factor)
	return t
	
for case in xrange(caseCount):
	line = raw_input()
	val = map(float, line.split(" "))
	cost = val[0]
	factor = val[1]
	target = val[2]
	print "Case #%d: %.7f" % (case+1, getOptimal(0, 2))
