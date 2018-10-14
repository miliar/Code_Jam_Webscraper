#!/usr/bin/python
"""

"""
import sys

def calculateCase(case):
	ynaomi = case[0][:]
	ynaomi.sort()
	yken = case[1][:]
	yken.sort()
	nnaomi = ynaomi[:]
	nken = yken[:]
	yused = []
	nleft = 0
	nright = 0
	kindexes = []
	for i in range(len(ynaomi)):
		n = ynaomi[i]
		for j in range(len(yken)):
			k = yken[j]
			if n > k and j not in kindexes:
				nleft += 1
				kindexes.append(j)
				break
	nindexes = []
	for i in range(len(nken)):
		k = nken[i]
		for j in range(len(nnaomi)):
			n = nnaomi[j]
			if k > n and j not in nindexes:
				nright += 1
				nindexes.append(j)
				break
	return [nleft, len(case[0]) - nright]

def cases(filename):
	inputfile = open(filename)
	isfirst = True
	nCase = 0
	cases = []
	box = []
	i = 0
	for line in inputfile:
		stripedLine = line.replace(' ', '@').strip().replace('@', ' ')
		if isfirst and stripedLine != '':
			nCase = int(stripedLine)
			isfirst = False
		elif isfirst == False:
			i += 1
			if i == 1:
				i
			elif i == 2:
				box.append([float(x) for x in stripedLine.split(' ')])
			elif i == 3:
				box.append([float(x) for x in stripedLine.split(' ')])
				cases.append( box[:] )
				box = []
				i = 0
	return cases
def writeResult2File(result, filename):
	text_file = open(filename, "w")
	text_file.write(result)
	text_file.close()

if __name__ == '__main__':
	cs = cases(sys.argv[1])
	print cs
	
	i = 0
	s = ''
	for case in cs:
		i += 1
		print i
		rcase = calculateCase(case)
		s += 'Case #%s: %s %s\n' %(i, rcase[0], rcase[1])
	writeResult2File(s, sys.argv[1] + '.out')
	print s
	
