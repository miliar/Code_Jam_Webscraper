#!usr/bin/env/python

from myFunctions import *

problem = 'b'
s_input = 'small'
s_id = 'lawnmower'


# problem = 'a'
# s_input = 'test'
# s_id = '0'
rownum = 0

n, cases = parseInputData(problem, s_input, s_id)
result = ""
# for i in range(4,len(cases),5):
# 	X,O,nil_flag = tttt_matrix(cases[i-4:i])
# 	result += "Case #%d: " %((i/5)+1) + str((tttt_sol(X,O,nil_flag))) + '\n'



for i in range(n):
	N, M = StrToNumList(cases[rownum])
	A = [StrToNumList(line) for line in cases[rownum + 1 : rownum + 1 + N]]
	rownum += N + 1
	result += "Case #%d: " %(i+1) + str(lawn_solve(A,N,M)) + '\n'

writeOutput(result, problem, s_input, s_id)
