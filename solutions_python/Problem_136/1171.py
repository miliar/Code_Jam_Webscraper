# Input data
infile = "B-large.in"
with open(infile, 'r') as f:
	data = f.read().split("\n")
while data[-1].isspace() or not(data[-1]):
	data.pop()
	
testCases = int(data[0])
dataL = data.__len__()

# Each case solution
c = 1 # Case iterator
results = []
while c < dataL:
	currentCase = data[c].split(" ")
	I = 2
	C = float(currentCase[0])
	F = float(currentCase[1])
	X = float(currentCase[2])
	factoryTime = 0.0
	totalTime = X/I
	prevTime = totalTime +1
	i = 0 # Strategy iterator
	while totalTime < prevTime:
		prevTime = totalTime
		factoryTime += C/(I+i*F)
		winTime = X/(I+(i+1)*F)
		totalTime = winTime + factoryTime
		i += 1
	results.append(prevTime)
	c+=1
	
#Output data
outfile = "out.txt"
with open(outfile, 'w') as f:
	for i in range(testCases):
		f.write("Case #%i: %f\n" % (i+1, results[i]))
