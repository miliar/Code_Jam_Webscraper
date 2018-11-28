import sys
import re
import itertools
from sets import Set
filename = sys.argv[1]
file = open(filename, 'r')
cases = int(file.readline())

def patrickSum(x,y):
	return x ^ y

def tryAllPossibleCombinationsOf(aList):
	bestSum = 0
	for i in range(1, (len(aList)/2)+1):
		groups = itertools.combinations(aList, i)
		for grp in groups:
			test = aList[:]
			for t in grp:
				test.remove(t)
			testSum = reduce(patrickSum, test)
			grpSum = reduce(patrickSum, grp)
			if (grpSum == testSum ) and (testSum != 0):
				realTestSum = sum(test)
				realGrpSum = sum(grp)
				if realTestSum > realGrpSum:
					if realTestSum > bestSum:
						bestSum = realTestSum
				else:
					if realGrpSum > bestSum:
						bestSum = realGrpSum
	return bestSum
	

for n in range(1, cases+1):
	candys = int(file.readline())
	data = map(lambda x: int(x), file.readline().strip('\n').split(' '))
	result = tryAllPossibleCombinationsOf(data)
	if result != 0:
		print 'Case #{}: {}'.format(n, result)
	else:
		print 'Case #{}: NO'.format(n)
		
		
		
	
		