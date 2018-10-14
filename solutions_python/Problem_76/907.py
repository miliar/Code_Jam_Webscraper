import sys
import itertools

def notList(fullList, body):
	for elem in body:
		fullList.remove(elem)
	return fullList

def sumUp(element1, element2):
	return (element1 + element2) - ((element1 & element2) * 2)

def listSumUp(elements):
	totalSum = elements[0]
	
	for i in xrange(1, len(elements), 1):
		totalSum = sumUp(totalSum, elements[i])

	return totalSum

def solve(elementCount, elements):
	highestValue = -1
	for i in xrange(1, elementCount, 1):
		#print i
		for combination in itertools.combinations(elements, i):
			#print combination
			#print notList(elements[:], combination)
			
			#print sum(notList(elements[:], combination))
			#print listSumUp(combination)
			if listSumUp(combination) == sum(notList(elements[:], combination)):
				# YEah! 
				if sum(combination) > highestValue:
					highestValue = sum(combination)
			
	
	return highestValue
	
if __name__ == "__main__":
	fd = open(sys.argv[1], "r")
	inputs = int(fd.readline()[:-1])
	
	for i in xrange(inputs):
		elementCount = int(fd.readline())
		elements = fd.readline().split(" ")
		elements = [int(xy) for xy in elements]
		
		res = solve(elementCount, elements)
		
		#print line
		if (res == -1):
			print "Case #%d: NO" % (i+1, )
		else:
			print "Case #%d: %d" % (i+1, res)
		
