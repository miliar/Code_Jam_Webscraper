import sys

f = open(sys.argv[1])
numProblems = int(f.readline())

for i in xrange(numProblems):
	numEngines = int(f.readline())
	engines = []
	for j in xrange(numEngines):
		engines.append(f.readline().strip())

	numTerms = int(f.readline())
	terms = []
	for j in xrange(numTerms):
		terms.append(f.readline().strip())

	count = 0
	while True:
		best = 0
		try:
			for e in engines:
				switch = terms.index(e)
				if switch > best:
					best = switch
			count += 1
			terms = terms[best:]
		except ValueError:
			# Not found, so done!
			break

	print 'Case #' + `i + 1` + ': ' + `count`
	
	

    