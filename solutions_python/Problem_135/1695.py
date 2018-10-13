#!/usr/bin/python

import sys

def cases(filename):
	inputfile = open(filename)
	isfirst = True
	nCase = 0
	cases = []
	case = []
	row1 = 0
	row2 = 0
	i = 0
	for line in inputfile:
		stripedLine = line.replace(' ', '@').strip().replace('@', ' ')
		if isfirst and stripedLine != '':
			nCase = int(stripedLine)
			isfirst = False
		elif isfirst == False:
			i += 1
			if i == 1:
				row1 = int(stripedLine)
			elif 2 <= i and i <= 5:
				if i == row1 + 1:
					case.append(stripedLine.split(' '))
			elif i == 6:
				row2 = int(stripedLine)
			elif 7 <= i and i <= 9:
				if i == row2 + 6:
					case.append(stripedLine.split( ' '))
			elif i == 10:
				if i == row2 + 6:
					case.append(stripedLine.split( ' '))
				i = 0
				cases.append(case[:])
				case = []
	return cases
def calculateCase(case):
	row1 = case[0]
	row2 = case[1]
	nSame = 0
	sameNumber = 0
	for i in row1:
		for j in row2:
			if i == j:
				nSame += 1
				sameNumber = i
	result = ""
	if nSame == 1:
		result = str(sameNumber)
	elif nSame == 0:
		result = "Volunteer cheated!"
	else:
		result = "Bad magician!"
	return result	
def writeResult2File(result, filename):
	text_file = open(filename, "w")
	text_file.write(result)
	text_file.close()

if __name__ == '__main__':
	cs = cases(sys.argv[1])
	i = 0
	s = ''
	for case in cs:
		i += 1
		s += 'Case #%s: %s\n' %(i, calculateCase(case))
	writeResult2File(s, sys.argv[1] + '.out')