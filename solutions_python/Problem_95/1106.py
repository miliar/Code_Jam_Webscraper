#!usr/bin/env/python

from myFunctions import *

problem = 'a'
s_input = 'small'
s_id = 'sit0'

'''
problem = 'a'
s_input = 'test'
s_id = '0'
'''
n, cases = parseInputData(problem, s_input, s_id)
result = ""
for i in range(0,n):
	result += "Case #%d: " %(i+1) + (googlerese(cases[i])) + '\n'

writeOutput(result, problem, s_input, s_id)