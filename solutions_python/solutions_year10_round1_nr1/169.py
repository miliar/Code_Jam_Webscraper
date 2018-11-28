#!/usr/bin/env python

def kRow(RowData, K, Dim):
	temp = set()
	
	for startRow in xrange(0,Dim):
		for startColumn in xrange(0,Dim-K+1):
			test = RowData[startRow][startColumn]
			if test == 0 or test in temp:
				continue
			for i in xrange(K):
				if test != RowData[startRow][startColumn + i]:
					break
			else:
				temp.add(test)
				if len(temp) == 2:
					return temp

	for startRow in xrange(0,Dim-K+1):
		for startColumn in xrange(0,Dim):
			test = RowData[startRow][startColumn]
			if test == 0 or test in temp:
				continue
			for i in xrange(K):
				if test != RowData[startRow + i][startColumn]:
					break
			else:
				temp.add(test)
				if len(temp) == 2:
					return temp

	for startRow in xrange(0,Dim-K+1):
		for startColumn in xrange(0,Dim-K+1):
			test = RowData[startRow][startColumn]
			if test == 0 or test in temp:
				continue
			for i in xrange(K):
				if test != RowData[startRow + i][startColumn + i]:
					break
			else:
				temp.add(test)
				if len(temp) == 2:
					return temp

	for startRow in xrange(0,Dim-K+1):
		for startColumn in xrange(K-1,Dim):
			test = RowData[startRow][startColumn]
			if test == 0 or test in temp:
				continue
			for i in xrange(K):
				if test != RowData[startRow + i][startColumn - i]:
					break
			else:
				temp.add(test)
				if len(temp) == 2:
					return temp
	return temp
	


def gravity(RowData, Dim):
	new = [[0 for i in xrange(Dim)] for i in xrange(Dim)]
	for x in xrange(Dim):
		data = []
		for y in xrange(Dim-1, -1, -1):
			if RowData[y][x] != 0:
				data.append(RowData[y][x])

		for y in xrange(len(data)):
			new[Dim - 1 - y][x] = data[y]
	return new

def rotate(RowData, K, Dim):
	new = [[0 for i in xrange(Dim)] for i in xrange(Dim)]
	for i, row in enumerate(RowData):
		for j, value in enumerate(row):
			new[j][Dim - 1 - i] = value
	test = gravity(new, Dim)

	#for i in test:
	#	for j in i:
	#		print j if j > 0 else " ",
	#	print
	temp = sorted(kRow(test, K, Dim))
	#print K, temp

	if len(temp) == 0:
		return "Neither"
	if len(temp) == 1:
		if temp[0] == 1:
			return "Red"
		else:
			return "Blue"
	return "Both"

def solve(RowData, K, Dim):
	return rotate(RowData, K, Dim)

def solveFile(Filename):
	inFile = file(Filename, "r")
	outFile = file(Filename[:-2]+"out", "w")
	numTestCases = int(inFile.readline())
	for i in xrange(1, numTestCases+1):
		dim,k = [int(num) for num in inFile.readline().split(" ")]
		data = []
		for line in xrange(dim):
			t = inFile.readline().strip()
			data.append([0 if char == "." else 1 if char == "R" else 2 for char in t])
		outFile.write("Case #%i: %s\n" %(i, solve(data,k,dim)))

solveFile("A-small-test.in")
#solveFile("A-small-attempt6.in")
solveFile("A-large.in")
