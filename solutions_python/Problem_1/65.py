def isJustFull(hitCount, query):
	zeroCount = 0
	lastZeroKey = ""
	for i in hitCount:
		if hitCount[i] == 0:
			zeroCount += 1
			lastZeroKey = i
	return (zeroCount == 1 and lastZeroKey == query)

def initHitCount(engines):
	result = {}
	for j in engines: result[j] = 0
	return result

def main():
	import sys
	numberOfInputs = int(sys.stdin.readline())
	for i in range(1, numberOfInputs+1):
		numberOfEngines = int(sys.stdin.readline())
		engines = []
		for j in range(numberOfEngines):
			engines.append(sys.stdin.readline())

		hitCount = initHitCount(engines)
		numberOfQueries = int(sys.stdin.readline())
		numberOfSwitches = 0

		for j in range(numberOfQueries):
			query = sys.stdin.readline()
			if isJustFull(hitCount, query):
				numberOfSwitches += 1
				hitCount = initHitCount(engines)
			if engines.count(query) > 0:
				hitCount[query] += 1

		print "Case #"+str(i)+": " + str(numberOfSwitches)

if __name__ == "__main__":main()
