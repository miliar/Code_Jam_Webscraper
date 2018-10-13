from __future__ import with_statement
#FILE = "a.input.small"
#FILE = "A-small-attempt1.in"
FILE = "A-large.in"

with file(FILE, 'r') as f:
	numberOfCases = int(f.readline())
	testCase = 0

	for testCase in range(1, numberOfCases + 1):
		numberOfEngines = int(f.readline())
		engines = []
		for _ in range(numberOfEngines):
			engines.append(f.readline().strip())

		numberOfQueries = int(f.readline())
		queries = []
		for _ in range(numberOfQueries):
			queries.append(f.readline().strip())

		switches = 0
		if len(queries) == 0: print "Case #%d: 0" % testCase
		while(len(queries) > 0):
			engineOneshot = engines[:]
			lastEnginePos = None
			for i in range(len(queries)):
				if queries[i] in engineOneshot:
					engineOneshot.remove(queries[i])
					
					if(len(engineOneshot) == 0):
						lastEnginePos = i
						break

			if not lastEnginePos:
				print "Case #%d: %d" % (testCase, switches)
				break

			switches += 1
			queries = queries[i:]

