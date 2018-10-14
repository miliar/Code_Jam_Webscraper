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

for i in range(0, testcases):
	
	(a, b, k) = map(int, lines[1+i].split(' '))
	
	aList = range(0, a)
	bList = range(0, b)
	
	import itertools as it
	
	test = map(lambda (x,y): x&y, it.product(aList, bList))
	
	t2 = map(lambda x: x<k, test)
	result = sum(t2)
	print result
	
	ret = "Case #"+str(i+1)+": "
	
	ret += str(result)
	
	outputDataFile.write(ret+"\n")

outputDataFile.close()