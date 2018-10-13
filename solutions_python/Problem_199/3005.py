#!/usr/bin/python

def flipper(string):
	returnValue = ''
	for i in string:
		if i=='-':
			returnValue += '+'
		else:
			returnValue += '-'
	return returnValue

def flip(string, index, k):
	returnValue = string[index+k:] if (index+k < len(string)) else ''
	return string[:index]+flipper(string[index:index+k])+returnValue

def isValid(string):
	if string[0] == '-':
		return False
	return True if (len(set(string)) == 1) else False

def solve():
	string, k = raw_input().strip().split()
	count = 0
	k = int(k)
	length = len(string)
	while not isValid(string):
		index = string.find('-')
		if index > length-k:
			return "IMPOSSIBLE"
		string = flip(string, index, k)
		count += 1
	return str(count)

for i in xrange(input()):
	print "Case #"+str(i+1)+": "+solve()
