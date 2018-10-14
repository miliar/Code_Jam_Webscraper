#!/usr/bin/python

import requests, logging, string, sys

multimap = {
	'11' : '1',
	'1i' : 'i',
	'1j' : 'j',
	'1k' : 'k',
	'i1' : 'i',
	'ii' : '-1',
	'ij' : 'k',
	'ik' : '-j',
	'j1' : 'j',
	'ji' : '-k',
	'jj' : "-1",
	'jk' : 'i',
	'k1' : 'k',
	'ki' : 'j',
	'kj' : '-i',
	'kk' : '-1'
}

def createOutput(result):
	f = open(sys.argv[2], "w")
	for i in range(0, len(result)):
		f.write("Case #" + str(i + 1) + ": " + result[i] + "\n")
	f.close();
	return

def multiply(a, b):
	negative = False
	if '-' in a:
		negative = not negative
		a = a.split('-')[1]

	if '-' in b:
		negative = not negative
		b = b.split('-')[1]

	result = multimap[a + b]

	if '-' in result:
		negative = not negative
		result = result.split('-')[1]

	if negative:
		return '-' + result
	else:
		return result


def processResults(L, X, textlist):
	usedInput = 0
	result = '1'
	length = len(textlist)
	expectedResult = ['i', 'j', 'k']
	excount = 0
	while usedInput < X:
		index = 0
		while index < length:
			result = multiply(result, textlist[index])
			index = index + 1
			if result == expectedResult[excount] and excount < 2:
				result = '1'
				excount = excount + 1
		usedInput = usedInput + 1
	if result == 'k' and excount == 2:
		return 'YES'
	else:
		return 'NO'

def processInput(inputlines):
	results = []
	for datamap in inputlines:
		L = datamap['L']
		X = datamap['X']
		text = datamap['text']
		result = processResults(L, X, list(text))
		results.append(result)
	return results

def readInput():
	inputlines = []
	f = open(sys.argv[1])
	testcases = int(f.readline().strip())
	for i in range(0, testcases):
		values = f.readline().strip().split(' ')
		datamap = {}
		datamap['L'] = int(values[0])
		datamap['X'] = int(values[1])
		datamap['text'] = f.readline().strip()
		inputlines.append(datamap)
	f.close()
	return inputlines

if __name__ == '__main__':
	inputlines = readInput()
	results = processInput(inputlines)
	createOutput(results)
	sys.exit()
