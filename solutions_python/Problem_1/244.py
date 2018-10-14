import sys

# Calculates a metric for a certain path
def calculate_metric(queries, current_engine, search_engines):

	# The first trivial case
	if queries is None: return 0

	# Find the first time we need to switch
	try:
		i = queries.index(current_engine)
	except ValueError:
		return 0

	# Get the sublist
	future_queries = queries[i:]

	# Use some heuristics to speed up the search (purely optional)
	choices = set(search_engines)
	for future_query in future_queries:
		if len(choices) == 1: break
		if future_query in choices: choices.remove(future_query)

	# Get the metrics
	metrics = [ calculate_metric(future_queries, engine, search_engines) for engine in choices ]
	
	# Return the smallest plus one for this hop
	return min(metrics) + 1

# Actually perform the testing
def run_test(input_file):

	# Open the file
	fp = open(input_file, "r")
	if fp is None: raise IOError, "Cannot open input file"
	lines = fp.readlines()
	lines = [ s.rstrip("\n") for s in lines ]
	fp.close()

	# Get the number of cases
	cases = int( lines[0] )

	# For each case
	fpos = 1
	for i in range(cases):

		# Get the number of search engines
		n_search_engines = int( lines[fpos] )
		fpos += 1

		# Grab the set of search engines
		search_engines = lines[fpos:fpos+n_search_engines]
		fpos += n_search_engines

		# Get the number of queries
		queries = int( lines[fpos] )
		fpos += 1

		# Find the best metric
		switches = calculate_metric( lines[fpos:fpos+queries], lines[fpos], search_engines )
		fpos += queries

		# Print the results
        	if not switches == 0: switches -= 1
		print "Case #%i: %i" % (i+1, switches)

sys.setrecursionlimit(1000000)
run_test(sys.argv[1])

