#!/bin/bash

def getListValues():
	return dict.values()

def checkValidaty(coord, value):
	i = 0

	validaty = True

	while True:
		coordTmp = (coord[0], i)
		i += 1
		if coordTmp in dict:
			valueTmp = dict[coordTmp]

			if valueTmp > value:
				validaty = False
				break
		else:
			break

	if validaty:
		return True

	i = 0

	while True:
		coordTmp = (i, coord[1])
		i += 1
		if coordTmp in dict:
			valueTmp = dict[coordTmp]

			if valueTmp > value:
				return False
		else:
			break

	return True

def processValue(i):
	for coord, value in dict.iteritems():
		if value == i:
			if not checkValidaty(coord, i):
				return False

	return True
			
def processGarden():
	values = getListValues()

	values.sort()	
	values = list(set(values))
	values.reverse()

	values = values[1:]

	for i in values:
		if not processValue(i):
			return False

	return True

dict = {}
numResolvedCases = 1

with open('lawnmower_test.txt', 'r') as f:
	numCases = 0
	n = 0
	m = 0
	nTmp = 0
	for i, line in enumerate(f):
		line = line.strip()
		optionsList = line.split(' ')

		if i == 0:
			numCases = int(line)
		elif (n != 0):

			for j in xrange(m):	
				dict[((nTmp - n), j)] = int(optionsList[j])

			n -= 1

			if n == 0:
				if not processGarden():
					print 'Case #%d: NO' % (numResolvedCases)
				else:
					print 'Case #%d: YES' % (numResolvedCases)
	
				numResolvedCases += 1
				
		else:
			n = int(optionsList[0])
			m = int(optionsList[1])
			dict = {}
			nTmp = n
			numCases += n

		if i == numCases:
			break;
