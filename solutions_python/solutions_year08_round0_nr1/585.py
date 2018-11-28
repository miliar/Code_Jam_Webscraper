import sys

def parse_input(file):
    """
        Yields (case number, [engines], [queries])
    """
    cases = int(file.readline()) # number of cases
    for c in xrange(1, cases+1):
        S = int(file.readline()) # number of engines
	engines = []
	for i in xrange(0,S):
	    engines.append(file.readline().rstrip('\n'))

	Q = int(file.readline()) # number of queries
	queries = []
	for i in xrange(0,Q):
	    queries.append(file.readline().rstrip('\n'))
	    
	yield c, engines, queries

if __name__ == "__main__":
    
    for c, engines, queries in parse_input(open(sys.argv[1], "r")):
	
	enginesnb = len(engines)
	unusables = set()   #The engines we cannot use
	                    #(unless we want the universe to implode)
	switches = 0        # count the number of engine switches
	for q in queries:
	    if q not in unusables:
		if len(unusables) == enginesnb-1:
		    switches+=1
		    unusables.clear()
		unusables.add(q)

        print "Case #%d: %d" % (c, switches)
