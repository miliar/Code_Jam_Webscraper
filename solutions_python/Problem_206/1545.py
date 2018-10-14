#!/usr/bin/python

import math
import collections

Hourse = collections.namedtuple('Hourse', ['K', 'S'])

class Storage:
	def __init__(self):
		self.destination = 0;
		self.horses = list()
	
	def info(self):
		print "Destination: {} len: {}".format(self.destination, len(self.horses))
		for horse in self.horses:
			print horse

def parseFile(inputPath):
	count = 0
	list = []
	
	s = None
	horseCount = 0
	try:
		with open(inputPath, 'r') as file:
			for line in file.readlines():
				count += 1
				if count==1:
					continue
			
				part = line.split()
				if not s or horseCount==0:
					s = Storage()
					list.append(s)
					s.destination = int(part[0])
					horseCount = int(part[1])
					continue
			
				tmp = Hourse(int(part[0]), int(part[1]))
				s.horses.append(tmp)
				horseCount -= 1

	except:
		print "Failed"

	return list

def solve(tuple):
	k = list(tuple[0])
	s = tuple[1]
	length = len(k)
	if length<s:
		return -1
	
	count = 0
	for i in xrange(0, (length-s+1)):
		if k[i]=='+':
			continue
		
		# Flip s times
		k[i] = '+'
		for j in xrange(1, s):
			if k[i+j]=='-':
				k[i+j] = '+'
			else:
				k[i+j] = '-'

		count += 1 # Count Flip time

	for i in xrange(length-s, length):
		if k[i]=='-':
			return -1

	return count

#inputPath = "/Users/Non/Documents/Work/CodeJam2017/1B/A/input.in"
#inputPath = "/Users/Non/Documents/Work/CodeJam2017/1B/A/A-small-attempt4.in"
inputPath = "/Users/Non/Documents/Work/CodeJam2017/1B/A/A-large.in"
outputPath = inputPath.replace(".in", ".out")

print "Input: {}".format(inputPath)
print "Output: {}".format(outputPath)

lines = parseFile(inputPath)

try:
	count = 0
	with open(outputPath, 'wb') as file:
		for line in lines:
#			line.info()
			count += 1

			dest = line.destination
			maxTime = 0
			for horse in line.horses:
				time = (dest - horse[0])/float(horse[1])
				if time>maxTime:
					maxTime = time
		
			result = dest/maxTime;
			res = "Case #%d: %.6f\n"%(count, result)
			file.write(res)
except:
	print "Write output failed"

#	print "Input number: {} last number: {}".format(n, res)
