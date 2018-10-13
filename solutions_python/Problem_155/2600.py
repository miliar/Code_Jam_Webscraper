# Input file
fname = "A-large"
inputfile = fname + ".in"
outputfilename = fname + ".out"
lines = [line.strip() for line in open(inputfile)]
# print lines

steps = int(lines.pop(0))
result = list()

# print lines
# Solution

for nTest in xrange(0, steps):
	currentLevel = 0
	pplStanding = 0
	pplNeedTotal = 0
	(maxLevel, audience) = lines[nTest].split(' ')
	audience = list(audience)
	for nLevel in xrange(0, len(audience)):
		pplInLevel = int(audience[nLevel])
		if (nLevel <= pplStanding):
			pplStanding += pplInLevel
		else: 
			pplNeed = nLevel - pplStanding 
			pplNeedTotal += pplNeed
			pplStanding += pplNeed + pplInLevel
	result.append(pplNeedTotal)

# Output file
# print result
outputfile = open(outputfilename, 'w')
for nCase in xrange(0, len(result)):
	outputfile.write("Case #%d: %d \n" % ((nCase + 1), (result[nCase])) )
