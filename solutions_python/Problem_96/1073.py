#! /usr/bin/env python

#imports here
from myFunctions import *

##########################################################################################################################
# Main code goes here
					
problem = 'B'
s_input = 'large'
s_id = 'dance'

nCase, inputList = parseInputData(problem, s_input, s_id)
result = []

for i in range(nCase):
	result.append("Case #%d: %s\n" %(i+1, danceScores(inputList[i])))

writeOutput(result, problem, s_input, s_id)

##########################################################################################################################
