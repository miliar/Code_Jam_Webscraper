#!/usr/bin/python2.7
import os
import sys
import string
import math
import itertools



data = open("A_input_large",'r').read().splitlines()
#Get number of cases and strip it
numCases = data[0]
data = data[1::]
#Start iterating
caseNum = 1
for case in data:
	case = string.split(case," ")
	#Get number of buttons and strip it
	numButtons = case[0]
	case = case[1::]
#	print ("Case #" + str(caseNum) + ":")
#	print case
	buttons = {}
	pos = {}
	buttons['O'] = []
	buttons['B'] = []
	pos['O'] = 1
	pos['B'] = 1
	seq = []
	i = 0
	while i < len(case)-1:
		buttons[case[i]].append(case[i+1])
		seq.append(case[i] + case[i+1])
		i += 2
#	print seq
#	print buttons
#	print pos
#	seconds = 0
#	for x in seq:
	seconds = 0
	i = 0
	while i < len(case)-1:
#		print buttons
	#	print pos[case[i]], case[i+1]
#		while(pos[case[i]] != int(case[i+1])):
		buttonPressed = False
		while(buttonPressed == False):
			seconds += 1
#			print "\nwaiting for robot",case[i],"to be at position",case[i+1]
#			print "robot",case[i],"currently at position",pos[case[i]]
#			print seconds,case[i],pos[case[i]], "!=",int(case[i+1])
#			print "BUT NEXT STEP IS", buttons[case[i]][0]
			for robot in ['O','B']:
				if(len(buttons[robot]) > 0):
#					print "robot",robot,"@",pos[robot],"but needs to be at",buttons[robot][0]
					if(pos[robot] < int(buttons[robot][0])):
						pos[robot] += 1
#						print seconds,robot,"Moving to",pos[robot]
					elif(pos[robot] > int(buttons[robot][0])):
						pos[robot] -= 1
#						print seconds,robot,"Moving to",pos[robot]
					elif((pos[robot] == int(buttons[robot][0])) and (case[i] == robot)):
#						print seconds,robot,"pressing button",pos[robot]
						buttonPressed = True
#					elif(pos[robot] == int(buttons[robot][0])):
#							print seconds,robot,"staying at",pos[robot]
#						print robot,"NOT MOVING"
#			if seconds > 6:
#				raise SystemExit
#			print "done waiting for robot",case[i],"to be at position",case[i+1]
#			print "robot",case[i],"currently at position",pos[case[i]]
		buttons[case[i]].pop(0)
		i += 2
	print ("Case #" + str(caseNum) + ": " + str(seconds))
	caseNum += 1
#	if caseNum > 1:
#		raise SystemExit
	

