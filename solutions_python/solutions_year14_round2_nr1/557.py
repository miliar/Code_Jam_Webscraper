from math import fabs

caseCount = int(raw_input())

def remove_repeat(line):
	result = [(line[0], 1)]
	for i in xrange(1,len(line)):
		if line[i] == result[-1][0]:
			result[-1] = (line[i], result[-1][1]+1)
		else:
			result.append((line[i], 1))
	#print result
	return result



def solveSmall(lines):
	data = []
	for line in lines:
		data.append(remove_repeat(line))
	l = len(data[0])
	for line in data:
		if len(line) != l:
			return "Fegla Won"
	changes = 0
	for i in xrange(l):
		avr = 0
		lenD = len(data)
		c = data[0][i][0]
		#print "Testing:",c
		for d in xrange(lenD):
			avr += data[d][i][1]
			if data[d][i][0] != c:
				return "Fegla Won"
		avr /= lenD
		for d in xrange(lenD):
			changes += fabs(data[d][i][1] - avr)
	return "%d" % changes


for case in xrange(caseCount): 
	line_count = int(raw_input())
	lines = []
	for i in xrange(line_count):
		lines.append(raw_input())
	print "Case #%d: %s" % (case+1,solveSmall(lines))