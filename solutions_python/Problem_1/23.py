testcase = """2
5
Yeehaw
NSM
Dont Ask
B9
Googol
10
Yeehaw
Yeehaw
Googol
B9
Googol
NSM
B9
NSM
Dont Ask
Googol
5
Yeehaw
NSM
Dont Ask
B9
Googol
7
Googol
Dont Ask
NSM
NSM
Yeehaw
Yeehaw
Googol"""

def numswitches(selist, qlist):
	m = 0
	semap = {}
	for s in selist:
		semap[s] = m
		m += 1
	qremaplist = [semap.get(q,-1) for q in qlist]

	currentset = set()
	n = 0
	for q in qremaplist:
		if q >= 0:
			currentset.add(q)
			if len(currentset) == m:
				n += 1
				currentset = set()
				currentset.add(q)
	return n

#lines = testcase.splitlines()
lines = open("A-large.in").readlines()
ntestcases = int(lines[0])
offset = 1
for i in xrange(ntestcases):
	nse = int(lines[offset])
	offset += 1
	selist = lines[offset:offset+nse]
	offset += nse
	nq = int(lines[offset])
	offset += 1
	qlist = lines[offset:offset+nq]
	offset += nq
	print "Case #%d: %d" % (i+1, numswitches(selist, qlist))

