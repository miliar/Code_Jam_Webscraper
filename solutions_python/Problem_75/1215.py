import sys

def alchemy(string,reductions,annihilations):
	accumulator = []
	for i in range(len(string)):
		accumulator.append(string[i])
		if len(accumulator) < 2:
			  continue
		x,y = accumulator[-2:]
		if (x,y) in reductions:
			accumulator = accumulator[:-2]+[reductions[(x,y)]]
		elif y in annihilations:
			opposed = annihilations[y]
			if opposed in accumulator:
				accumulator= []
	strres = "["
	for x in accumulator:
		strres += x+", "
	if strres == "[":
		return "[]"
	return strres[:-2]+"]"

def parse_input(filename):
	file = open(filename)
	file.readline()

	result = []
	for line in file:
		reductions = {}
		annihilations = {}	
		splitline = line.strip().split(" ")
		rcount = int(splitline[0])
		for reduction in splitline[1:(1+rcount)]:
			reductions[(reduction[0],reduction[1])]=reduction[2]
			reductions[(reduction[1],reduction[0])]=reduction[2]
		offset = rcount+1
		anncount = int(splitline[offset])
		for ann in splitline[(offset+1):(offset+1+anncount)]:
			annihilations[ann[0]] = ann[1]
			annihilations[ann[1]] = ann[0]
		string = splitline[-1]
		result.append((string,reductions,annihilations))
	return result

for i,case in enumerate(parse_input(sys.argv[1])):
	string,red,ann= case
	print "Case #"+str(i+1)+":",alchemy(string,red,ann)
