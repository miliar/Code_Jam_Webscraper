#! /usr/bin/env python

#imports here
from myFunctions import *

##########################################################################################################################

# Main code goes here
					
problem = 'A'
s_input = 'small'
s_id = 'magic'

first, rest = parseInputData_gen(problem, s_input, s_id)
N = StrToNum(first)
cases = map(StrToNumList, rest)

result = []

for i in range(N):
	result.append("Case #%d: %s\n" %(i+1, magic_trick(cases[i*10:10*(i+1)])))

writeOutput(result, problem, s_input, s_id)

##########################################################################################################################5

