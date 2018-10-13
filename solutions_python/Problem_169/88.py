def twostreams(v,t,ra,xa,rb,xb):
	if max(xa,xb) < t or min(xa,xb) > t:
		return 'IMPOSSIBLE'
	if xa == t:
		if xb == t:
			return v/(ra+rb)
		else:
			return v/ra
	if xb == t:
		return v/rb
	ratio = (xa-t)/(t-xb)
	va = v/(1+ratio)
	vb = v*ratio/(1+ratio)
	return max((va/ra),(vb/rb))

def onestream(v,t,r,x):
	if x != t:
		return 'IMPOSSIBLE'
	return v/r
	
import sys

with open(sys.argv[1], "r") as fileIN:
	inputLines = fileIN.readlines()

inputLines = [line.strip() for line in inputLines]	

with open(sys.argv[2], "w") as fileOUT:
	numberOfCases = int(inputLines.pop(0))
	for num in range(numberOfCases):	
		specs = [float(y) for y in inputLines.pop(0).rstrip().rsplit(' ')]
		streams,v,t = specs
		streams = int(streams)
		if streams == 1:
			r,x = [float(y) for y in inputLines.pop(0).rstrip().rsplit(' ')]
			output = onestream(v,t,r,x)
		if streams == 2:
			ra,xa = [float(y) for y in inputLines.pop(0).rstrip().rsplit(' ')]
			rb,xb = [float(y) for y in inputLines.pop(0).rstrip().rsplit(' ')]
			output = twostreams(v,t,ra,xa,rb,xb)
		fileOUT.write('Case #' + str(num+1) + ': ' + str(output) + '\n')