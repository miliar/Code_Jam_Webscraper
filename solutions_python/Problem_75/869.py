import math

def checkCombine(elements, combine):
	eSize=len(elements)
	change = False
	if eSize > 1:
		e1 = elements[eSize-1]
		e0 = elements[eSize-2]
		
		noCombine=len(combine)
		for i in range(0,noCombine):
			combo=combine[i]
			if (change==False and  ( (e1==combo[1] and e0==combo[0]) or (e1==combo[0] and e0==combo[1]) ) ):
				del elements[eSize-2:eSize]
				elements.append(combo[2])
				change=True
				break
	return change
	
def checkDestroy(elements, destroy):
	eSize=len(elements)
	change = False
	
	if eSize > 1:			
		noDestory=len(destroy)
		newE = elements[eSize-1]
		for i in range(0,noDestory):
			combo=destroy[i]
			if (change==False and  ( newE==combo[0] and combo[1] in elements) or (newE==combo[1] and combo[0] in elements) ):
				del elements[:]
				change = True
				break
	return change
			
			
directory = "/Users/se/Downloads/"

inFile=directory+"B-large.in"
outfile = directory+"test.out"

input = open(inFile)
output = open(outfile, "w")

line = input.readline().strip()
cases = int(line)

for case in range (0, cases):
	
	line = input.readline().strip().split(' ')
	noCombine = int(line[0])
	combineArray = []
	for i in range(0,noCombine):
		combineArray.append(list(line[i+1]))
		
	noOppose = int(line[noCombine+1])
	opposeArray = []
	for i in range(0,noOppose):
		opposeArray.append(list(line[i+noCombine+2]))
	
	noElements = int(line[noCombine+noOppose+2])
	elementString=list(line[noCombine+noOppose+3])
	
	finalString=[elementString[0]]
	for i in range(1, noElements):
		finalString.append(elementString[i])
		combined = checkCombine(finalString, combineArray)
		if (combined==False):
			checkDestroy(finalString, opposeArray)
	
	out = "["
	if len(finalString)>0:
		for i in range(0, len(finalString)-1): 
			out+=finalString[i]+", "
		out+=finalString[len(finalString)-1]
	out+="]"
	print >> output, "Case #%d: %s"%(case+1, out)
	