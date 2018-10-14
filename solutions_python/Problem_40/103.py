#!/usr/bin/env python2.6

def readCase(line):
	rslt = []
	chrlist = list(line)
	while len(chrlist) > 0:
		chr = chrlist.pop(0)
		if chr != "(":
			rslt.append([chr])
		else:
			inBrackets = []
			chr = chrlist.pop(0)
			while chr != ")":
				inBrackets.append(chr)
				chr = chrlist.pop(0)
			rslt.append(inBrackets)
	return rslt

def countPossibilities(alienWords, charList):
	rslt = 0
	for alienWord in alienWords:
		if compare(alienWord, charList):
			rslt += 1
	return rslt

def compare(alienWord, charList):
	for i in range(len(alienWord)):
		alienChar = alienWord[i]
		possibleChars = charList[i]
		if not possibleChars.count(alienChar):
			return False
	return True

def readAnimals(lines):
	lst = []
	for line in lines:
		words = line.split(" ")
		lst.append(words[2:])
	return lst

def calcTree(lines):
	tree = []
	node = []
	str = " ".join(lines)
	n1 = str.find("(")
	n2 = str.rfind(")")
	str = str[n1+1:n2]
	n3 = str.find(" ")
	if n3 == -1:
		return [float(str), "_"]

def calcCute(animal, treeLines):
	cuteness = 1.0
	pos = 0
	#indent = 0
	while True:
		line = treeLines[pos]
		i_open = line.find("(")
		i_close = line.find(")")
		words = line[i_open+1:].split(" ")
		if i_close != -1:
			cuteness *= float(line[i_open+1:i_close])
			return cuteness
		#indent += 2
		cuteness *= float(words[0])
		test = words[1]
		if test in animal:
			pos += 1
		else:
			indent = 0
			while True:
				pos += 1
				line = treeLines[pos]
				indent += line.count("(") - line.count(")")
				if indent == 0:
					pos += 1
					break


import sys
lines = sys.stdin.read().split("\n")

numTestCases = int(lines[0])
lines = lines[1:]

for testCase in range(numTestCases):
	numLines1 = int(lines[0])
	treeLines = lines[1:1+numLines1]
	numLines2 = int(lines[1+numLines1])
	animalLines = lines[numLines1+2:numLines1+2+numLines2]
	lines = lines[numLines1+2+numLines2:]
	
	#decisionTree = calcTree(treeLines)
	animals = readAnimals(animalLines)
	print "Case #" + str(testCase + 1) + ":"
	for animal in animals:
		cuteness = calcCute(animal, treeLines)
		print "%.7f" % cuteness
