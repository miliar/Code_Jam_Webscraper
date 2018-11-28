#!/usr/bin/python

import math
import collections

Tuple = collections.namedtuple('Tuple', ['N', 'K'])
Result = collections.namedtuple('Result', ['Max', 'Min'])

def parseFile(inputPath):
	count = 0
	lines = []
	try:
		with open(inputPath, 'r') as file:
			for line in file.readlines():
				if count==0:
					count += 1
					continue
			
				part = line.split()
				tmp = Tuple(int(part[0]), int(part[1]))
				lines.append(tmp)
				count += 1

	except:
		print "Failed"

	return lines

def isEven(num):
	return num%2==0

def getMaxNumPos(list):
	num = 0
	pos = 0
	for i in xrange(0, len(list)):
		if list[i]>num:
			pos = i
			num = list[i]

	return pos

def solve2(tuple):
	n = tuple[0]
	k = tuple[1]
	
	tempList = []
	tempList.append(n)
	for i in xrange(0, k):
		number = tempList[i]
		new = number/2
		tempList.append(new)
		if isEven(number):
			tempList.append(new-1)
		else:
			tempList.append(new)

	pos = k-1

#	print tempList
#	print "List length: {}".format(len(tempList))
#	print "Last number pos: {} number: {}".format(pos, tempList[pos])
	sortedList = sorted(tempList, reverse=True)
#	print sortedList
	lastNumber = sortedList[pos]
#	lastNumber = tempList[pos]
	if lastNumber==0:
		maxNum = minNum = 0
	else:
		if isEven(lastNumber):
			newNum = lastNumber/2
			maxNum = newNum
			minNum = newNum-1
		else:
			newNum = (lastNumber-1)/2
			maxNum = minNum = newNum
	
#	print "Last number: {} max num: {} min num: {}".format(lastNumber, maxNum, minNum)
	return Result(maxNum, minNum)


def solve(tuple):
	n = tuple[0]
	k = tuple[1]
	tempList = []
	tempList.append(n)
	for i in xrange(0, k-1):
		maxSpace = max(tempList)
		if isEven(maxSpace):
			newSpace = maxSpace/2
			tempList.remove(maxSpace)
			tempList.append(newSpace-1)
			tempList.append(newSpace)
		else:
			newSpace = (maxSpace-1)/2
			tempList.remove(maxSpace)
			tempList.append(newSpace)
			tempList.append(newSpace)

	maxSpace = max(tempList)
	if isEven(maxSpace):
		newSpace = maxSpace/2
		maxNum = newSpace
		minNum = newSpace-1
	else:
		newSpace = (maxSpace-1)/2
		maxNum = minNum = newSpace

#	print "Max space: {} max num: {} min num: {}".format(maxSpace, maxNum, minNum)
	return Result(maxNum, minNum)



#inputPath = "/Users/Non/Documents/Work/CodeJam2017/C/input.in"
#inputPath = "/Users/Non/Documents/Work/CodeJam2017/C/C-small-1-attempt0.in"
inputPath = "/Users/Non/Documents/Work/CodeJam2017/C/C-small-2-attempt2.in"
outputPath = inputPath.replace(".in", ".out")

print "Input: {}".format(inputPath)
print "Output: {}".format(outputPath)

lines = parseFile(inputPath)
#print lines

line = Tuple(500, 116)
#line = Tuple(999999, 262144)
#result = solve(line)
#print "Result: {}".format(result)

#result = solve2(line)
#print "Result: {}".format(result)

try:
	count = 0
	with open(outputPath, 'wb') as file:
		for line in lines:
			count += 1
			result = solve2(line)
			res = "Case #{}: {} {}\n".format(count, result[0], result[1])
			file.write(res)
except:
	print "Write output failed"

#	print "Input number: {} last number: {}".format(n, res)
