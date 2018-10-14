import sys

def main(filename):
	inputFile = open(filename)
	cases = int(inputFile.readline().strip())
	results = []
	for case in range(cases):
		switchCount = 0
		engines = []
		engineCount = int(inputFile.readline().strip())
		if engineCount < 2:
			print "Too few engines!"
			return
		for e in range(engineCount):
			engines.append(inputFile.readline().strip())
		queries = []
		queryCount = int(inputFile.readline().strip())
		for q in range(queryCount):
			queries.append(inputFile.readline().strip())
		qualEngines = []
		for e in engines:
			qualEngines.append(e)
		for q in queries:
			if q in qualEngines:
				engIndex = engines.index(q)
				if len(qualEngines) == 1:
					switchCount += 1
					qualEngines[0] = engines[0]
					for e in engines:
						qualEngines.append(e)
					qualEngines.remove(engines[0])
					qualEngines.remove(q)
				else:
					qualEngines.remove(q)
		results.append((case, switchCount))
	inputFile.close()
	return results
		
	

if __name__ == "__main__":
	results = main(sys.argv[1])
	for r in results:
		print 'Case #' + str(r[0]+1) + ': ' + str(r[1])
