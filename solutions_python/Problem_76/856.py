#!/usr/bin/python2.7
import string
import itertools


def pSum(candy):
	if(len(candy) == 0):
		return 0
	x = candy[0]
	i = 1
	while(i<len(candy)):
		x = x ^ candy[i]
		i += 1
	return x

def pAdd(a,b):
	#print a,"XOR",b,"=",a^b
	# I see what you did there...
	return (a ^ b)

data = open("C_small_input",'r').read().splitlines()
#Get number of cases and strip it
numCases = data[0]
#Get just the cases
data = data[2::2]
#Start iterating
caseNum = 1
for case in data:
	maxSum = -1
	case = string.split(case," ")
	data = []
	for c in case:
		data.append(int(c))
	data.sort()
#	print "SEAN",sum(sean),"PATRICK",sum(patrick)
	binary = [0,1]
	for it in itertools.product(range(2), repeat = len(data)):
		patrick = []
		sean = []
		index = 0
		for i in it:
			if(not(0 in it and 1 in it)):
				break
			if(i == 0):
				sean.append(data[index])
			else:
				patrick.append(data[index])
			index += 1
		if(pSum(sean) == pSum(patrick)):
			win = sum(sean)
			if(win > maxSum):
				maxSum = win
	if(maxSum > 0):
		print ("Case #" + str(caseNum) + ": " + str(maxSum))
	else:
		print ("Case #" + str(caseNum) + ": NO")
	caseNum += 1

	


