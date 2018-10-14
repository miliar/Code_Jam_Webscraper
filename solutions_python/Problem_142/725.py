import sys

#if len(sys.argv) > 1:

fileLocation = sys.argv[1].strip()
inputDataFile = open(fileLocation, 'r')

inputData = ''.join(inputDataFile.readlines())
inputDataFile.close()

outputDataFile = open(fileLocation+"_out", 'w')
	
#parse the input
lines = inputData.split('\n')

testcases = int(lines[0])

counter = 1

for a in range(0, testcases):
	
	numStrings = int(lines[counter])
	counter += 1
	
	stringList = []
	
	for i in range(0, numStrings):
		stringList.append(str(lines[counter]))
		counter += 1
	
	print stringList
	
	import itertools as it
	
	iterlist = map(it.groupby, stringList)
	tuplelist = map(lambda z: map(lambda (x, y): (x, len(list(y))), z), iterlist)
	
	strings = map(lambda z: map(lambda (x,y): x, z), tuplelist)
	counts = map(lambda z: map(lambda (x,y): y, z), tuplelist)
	print counts
	
	avg = map(sum, zip(*counts))
	avg = map(lambda x: int(round(1.0*x/numStrings)), avg)
	print avg
	
	import operator
	
	ret = "Case #"+str(a+1)+": "
	#magic!
	
	if not all(s == strings[0] for s in strings):
		ret += "Fegla Won"
	else:
		diffFromAvg = map(lambda x: map(operator.sub, x, avg), counts)
		diffFromAvg = map(lambda x: sum(map(abs, x)), diffFromAvg)
		print diffFromAvg
		
		moves = sum(diffFromAvg)
		
		ret += str(moves)
	
	print ret
	outputDataFile.write(ret+"\n")

outputDataFile.close()