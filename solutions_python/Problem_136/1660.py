#!/usr/bin/python
"""

"""
import sys
def calculateShortestTime(case, prefTime, nFarm):
	P = 2 # PER SECOND
	C = case[0] # FARM COST
	F = case[1] # EXTRA PER SECOND
	X = case[2] # TARGET
	thisTime = 0.0
	for i in range(nFarm):
		for j in range(i):
			thisTime += C / (P + j * F)
		thisTime += X / (P + i * F)
		#print 'X / (P + i * F) : %s / (%s + %s * %s) ' % (X, P, i, F)
		#print 'i: %s, thisTime : %s , prefTime: %s' % (i, thisTime, prefTime)
		if thisTime + 0.00000001 >= prefTime :
			return prefTime
		else:
			prefTime = thisTime
			thisTime = 0.0
#	elif nFarm == 995:
#		return thisTime
#		else:
#			return calculateShortestTime(case, thisTime, nFarm + 1)
def cases(filename):
	inputfile = open(filename)
	isfirst = True
	nCase = 0
	cases = []
	for line in inputfile:
		stripedLine = line.replace(' ', '@').strip().replace('@', ' ')
		if isfirst and stripedLine != '':
			nCase = int(stripedLine)
			isfirst = False
		elif isfirst == False:
			cases.append([float(x) for x in stripedLine.split(' ')])
	return cases
def writeResult2File(result, filename):
	text_file = open(filename, "w")
	text_file.write(result)
	text_file.close()

if __name__ == '__main__':
	cs = cases(sys.argv[1])
	i = 0
	s = ''
	for line in cs:
		i += 1
		s += 'Case #%s: %.7f\n' %(i, calculateShortestTime(line, 100000, 20000000))
	writeResult2File(s, sys.argv[1] + '.out')
