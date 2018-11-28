def gcd(a, b):
	smaller = min(a, b)
	larger = max(a, b)
	
	while (smaller != 0):
		remainder = larger % smaller
		larger = smaller
		smaller = remainder
		
	return larger

def main():
	fin = open("warning.in", "rt")
	fout = open("warning.out", "wt")
	
	nTestCases = int(fin.readline())
	
	for testNo in range(nTestCases):
		nEvents, eventsStr = fin.readline().split(None, 1)
		nEvents = int(nEvents)
		events = map(long, eventsStr.split());

		closestEventTime = min(events)
		
		
		gcdSoFar = 0L
		
		for evtA in events:
			for evtB in events:
				difference = abs(evtA - evtB)
				gcdSoFar = gcd(gcdSoFar, difference)

		
		nextTime = 0L;
		if (gcdSoFar != 0):
			nextTime = (gcdSoFar - (closestEventTime % gcdSoFar)) % gcdSoFar
			
		fout.write("Case #{0}: {1}\n".format(testNo+1, nextTime))	
		
	
main()
