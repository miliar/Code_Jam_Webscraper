from __future__ import with_statement
import math


def processFile(f, outf):
	numCases = int(f.readline())
	for caseNumber in xrange(1, numCases + 1):
		engines = set()
		for j in xrange(int(f.readline())):
			engines.add(f.readline().strip())
		queries = []
		for j in xrange(int(f.readline())):
			queries.append(f.readline().strip())

		if len(queries) > 0:
			darray = [-1 for i in xrange(len(queries))]
			
			switchset = set()
			for i, q in enumerate(queries):
				switchset.add(q)
				if len(switchset) < len(engines):
					darray[i] = 0
				else:
					break
			
			while darray[-1] < 0:
				if caseNumber == 10:
					print darray
				newarray = list(darray)
				for start, switches in enumerate(darray):
					if switches < 0:
						break
					switchset = set()
					switches += 1
					
					for i, q in enumerate(queries[start + 1:]):
						switchset.add(q)
						i = i + start + 1 
						if len(switchset) < len(engines):
							if newarray[i] < 0 or newarray[i] > switches:
								newarray[i] = switches
						else:
							break
				darray = newarray
			print >> fout, "Case #" + str(caseNumber) + ": " + str(darray[-1])
		else:
			print >> fout, "Case #" + str(caseNumber) + ": " + "0"


input = "A-large"
with open(input + ".in") as f:
	with open(input + ".out", "w") as fout:
		processFile(f, fout)
print "OK!"