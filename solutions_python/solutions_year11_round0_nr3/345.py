#!/usr/bin/env python

global debug, data

def eval():
	global debut, data

	#test if possible
	x = data[0]
	sum = data[0]
	for i in range(1,len(data)):
		x ^= data[i]
		sum += data[i]
	if (x != 0):
		return 0

	#test single digits
	for i in range(0,len(data)):
		x = -1
		for j in range (0, len(data)):
			if (debug): print "[%d,%d] =" % ( data[i], data[j]),
			if (i == j):
				if (debug): print "continue"
				continue
			elif (x == -1):
				if (debug): print "%s (init)" % bin(data[j])
				x = data[j]
			else:
				x ^= data[j]
				if (debug): print "%s (comp)" % bin(x)
		if (data[i] == x):
			return sum - data[i]
	return -1

def main():
	global debug, data
	debug = False
	cases = int(raw_input())

	for n in range(1,cases+1):
		data = []

		raw_input() #get rid of data size
		data = [ int(x) for x in raw_input().split() ]
		data.sort()
		if (debug):
			print data

		answer = eval()
		print "Case #%s:" % n,
		if (answer):
			print answer
		else:
			print "NO"

	return 0

main()
