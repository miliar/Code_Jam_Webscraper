#! /usr/bin/env python

#imports here
from myFunctions import *

##########################################################################################################################
# Main code goes here
					
problem = 'C'
s_input = 'small'
s_id = 'recnum'

nCase, inputList = parseInputData(problem, s_input, s_id)
result = []

for i in range(nCase):
	result.append("Case #%d: %s\n" %(i+1, recNum(inputList[i])))

writeOutput(result, problem, s_input, s_id)

##########################################################################################################################
