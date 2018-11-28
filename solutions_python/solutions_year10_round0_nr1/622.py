#!/usr/bin/env python
# -*- coding: utf-8 -*-

inputf = open('A-large.in','r')
outputf = open('A-large.out','w')
lineNumber = inputf.readline()
for i in range(int(lineNumber)):
	inputData = inputf.readline().split(' ')
	if((int(inputData[1])+1) % (2 << int(inputData[0])-1) == 0):
		state = 'ON'
	else :
		state = 'OFF'
	outputf.write('Case #%d: %s\n'%(i+1,state))
