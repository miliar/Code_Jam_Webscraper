import bisect

f = open("C-small-1-attempt0.in",'r')
f1 = open("output.out", "a")

numberOfCases = int(f.readline())
inputs = []

for i in xrange(1,numberOfCases+1):
	inputs.append(map(int,f.readline().split(' ')))

for i in xrange(0,len(inputs)):
	stalls = inputs[i][0]
	people = inputs[i][1]
	res = [0, stalls+1]
	
	while (people > 1):
		temp = [(res[x+1] - res[x]) for x in xrange(0,len(res)-1)]
		value = max(temp)
		bisect.insort(res, res[temp.index(value)] + int(value / 2))
		people -= 1

	temp = [(res[x+1] - res[x]) for x in xrange(0,len(res)-1)]
	value = max(temp)
	finalVal = res[temp.index(value)] + int(value / 2)
	bisect.insort(res, res[temp.index(value)] + int(value / 2))
	insertedIndex = res.index(finalVal)

	maxResult = res[insertedIndex+1] - finalVal - 1
	minResult = finalVal - res[insertedIndex-1] - 1
	f1.write("Case #" + str(i+1) + ": " + str(maxResult) + " " + str(minResult) + "\n")