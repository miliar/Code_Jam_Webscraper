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

for a in range(0, testcases):
	
	[C, F, X] = map(float, lines[1+a].split(' '))
	print C, F, X
	
	time = 0.0
	c_s = 2.0
	
	while True:
		
		nextFarm = C/c_s
		
		finished = X/c_s
		buyFinished = nextFarm + X/(c_s+F)
		
		if buyFinished <= finished:
			time += nextFarm
			c_s += F
		else:
			time += finished
			break
	
	ret = "Case #"+str(a+1)+": "+str(time)
	
	print ret
	outputDataFile.write(ret+"\n")

outputDataFile.close()