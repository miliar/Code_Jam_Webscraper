#!usr/bin/env/python

from myFunctions import *

problem = 'c'
s_input = 'large1'
s_id = 'fairsquare'


# problem = 'a'
# s_input = 'test'
# s_id = '0'
rownum = 0

n, cases = parseInputData(problem, s_input, s_id)
result = ""
# for i in range(4,len(cases),5):
# 	X,O,nil_flag = tttt_matrix(cases[i-4:i])
# 	result += "Case #%d: " %((i/5)+1) + str((tttt_sol(X,O,nil_flag))) + '\n'


p = gen_palindromes()
# print len(p)

for i in range(n):
	A, B = StrToNumList(cases[rownum])
	C, D = math.sqrt(A), math.sqrt(B)
	rownum += 1
	result += "Case #%d: " %(i+1) + str(palindrome_num(C,D,p)) + '\n'

writeOutput(result, problem, s_input, s_id)
