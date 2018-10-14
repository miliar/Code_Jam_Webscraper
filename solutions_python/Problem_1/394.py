def find(l, x):
	for i in range(0, len(l)):
		if l[i] == x:
			return i
	return -1

def findLatest(l, engines):
	max = -1
	maxEngine = ""
	for engine in engines:
		pos = find(l, engine)
		if pos > max:
			max = pos
			maxEngine = engine
	return max

def findOptimal(queries, engines):
	if len(engines) > len(set(queries)):
		return 0
	return 1 + findOptimal(queries[findLatest(queries, engines):], engines)

filename = raw_input()
f = open(filename, 'r')
cases = int(f.readline())
for caseid in range(1, cases+1):
	numEngines = int(f.readline())
	engines = []
	for engine in range(0, numEngines):
		engines = engines + [f.readline()]
	numQueries = int(f.readline())
	queries = []
	for query in range(0,numQueries):
		queries = queries + [f.readline()]
	print "Case #%d: %d" % (caseid, findOptimal(queries, engines))
