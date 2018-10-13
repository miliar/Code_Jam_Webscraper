#!/usr/bin/python2.7
import string
import pprint


data = open("B_input_small",'r').read().splitlines()
#Get number of cases and strip it
numCases = data[0]
data = data[1::]
#Start iterating
caseNum = 1
for case in data:
	case = string.split(case," ")
	combine = []
	oppose = []
	##################################
	numCombine = int(case[0])
	case = case[1:]
	if(numCombine > 0):
		combine = case[0:numCombine]
		case = case[numCombine:]
	##################################
	numOppose = int(case[0])
	case = case[1:]
	if(numOppose > 0):
		oppose = case[0:numOppose]
		case = case[numOppose:]
	##################################
	#numInvoke = int(case[0])
	#case = case[1:]
	invoke = case[1]
	##################################
	combinations = {}
	for x in combine:
		combinations[x[0:2]] = x[2]
		combinations[x[1::-1]] = x[2]
	##################################
	opposes = {}
	for x in oppose:
		opposes[x[0]] = x[1]
		opposes[x[1]] = x[0]

#	print ("Case #" + str(caseNum) + ":")
#	print "\nCombine",combine
#	print "Oppose",oppose
#	print "Invoke",invoke
#	print "Combinations",combinations
#	print "Opposes",opposes

	spell = []
	for x in invoke:
		if(len(spell) == 0):
			spell.append(x)
		else:
			if((x + spell[-1]) in combinations):
				last = spell.pop()
				spell.append(combinations[x + last])
			elif(x in opposes):
				if(opposes[x] in spell):
					del spell[:]
				else:
					spell.append(x)
			else:
				spell.append(x)
	print ("Case #" + str(caseNum) + ': [' + ', '.join(spell) + ']')
	caseNum += 1

	


