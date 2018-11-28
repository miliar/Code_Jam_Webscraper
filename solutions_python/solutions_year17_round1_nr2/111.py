import math

def kitrange(x,y):
	lower = math.ceil((10*y)/(11*x))
	upper = math.floor((10*y)/(9*x))
	return [lower,upper]
	
def legal(interval):
	return (interval[0] <= interval[1] and interval[1] > 0) 

def rangifylist(l,req):
	return sorted([kitrange(req,x) for x in l if legal(kitrange(req,x))])
	
def rangifymatrix(m,reqlist):
	return [rangifylist(m[k],reqlist[k]) for k in range(len(m))]

def overlap(interval1,interval2):
	return not(interval1[0] > interval2[1] or interval2[0] > interval1[1])

def listoverlap(l):
	return max([interval[0] for interval in l]) <= min([interval[1] for interval in l])

def positionofminimum(l):
	m = min(l)
	for k in range(len(l)):
		if l[k] == m:
			return k
	
def f(rangematrix):
	# print(rangematrix)
	if len(rangematrix) == 1:
		# print(len(rangematrix[0]))
		return len(rangematrix[0])
	count = 0
	while True:
		# print(rangematrix)
		# print(count)
		if min([len(rangematrix[k]) for k in range(len(rangematrix))]) == 0:
			return count
		candidates = [rangematrix[k][0] for k in range(len(rangematrix))]
		if listoverlap(candidates):
			count += 1
			for k in range(len(rangematrix)):
				rangematrix[k] = rangematrix[k][1:]
		else:
			m = positionofminimum(candidates)
			rangematrix[m] = rangematrix[m][1:]

import sys
with open(sys.argv[1], "r") as fileIN:
	inputLines = fileIN.readlines()
		
with open(sys.argv[2], "w") as fileOUT:
	numberOfCases = int(inputLines.pop(0))
	for num in range(numberOfCases):
		firstInput = [int(x) for x in inputLines.pop(0).rstrip().split()]
		numberOfIngredients = firstInput[0]
		numberOfPackages = firstInput[1]
		reqList = [int(x) for x in inputLines.pop(0).rstrip().split()]
		packetList = []
		for k in range(numberOfIngredients):
			packetList.append([int(x) for x in inputLines.pop(0).rstrip().rsplit()])
		fileOUT.write('Case #' + str(num+1) + ': ' + str(f(rangifymatrix(packetList,reqList))) + '\n')