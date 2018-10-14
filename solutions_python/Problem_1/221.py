def findBestEngine(engines, queries_remaining):
	best_number = -1
	best_engine = ""
	for engine in engines:
		if queries_remaining.count(engine) == 0:
			return engine
		no_of_queries = queries_remaining.index(engine)
		if no_of_queries > best_number:
			best_number = no_of_queries
			best_engine = engine
	return best_engine
		


f_in = open("A-large.in")
N = int(f_in.readline().rstrip())
for test_case in range(N):
	engines = []
	queries = []
	S = int(f_in.readline().rstrip())
	for search_engine in range(S):
		engines.append(str(f_in.readline().rstrip()))
	Q = int(f_in.readline().rstrip())
	switches = 0
	if Q > 0:
		for query in range(Q):
			queries.append(str(f_in.readline().rstrip()))
		current_engine = findBestEngine(engines, queries)
		while len(queries) > 0:
			if queries[0] == current_engine:
				current_engine = findBestEngine(engines, queries)
				switches = switches + 1
			queries.pop(0)
	print "Case #%d: %d" %(test_case+1, switches)
