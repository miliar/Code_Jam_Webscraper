#! /usr/bin/env python

#imports here
def parseInputData(problem, s_input, s_id):
	finput = open(problem + '-' + s_input + '-' + s_id + '.in','r')
	nCase = int(finput.readline().strip())
	inputList = finput.readlines()	
	finput.close()
	return nCase, inputList

##########################################################################################################################

def writeOutput(result, problem, s_input, s_id):
	foutput = open(problem + '-' + s_input + '-' + s_id + '.out','w')
	foutput.writelines(result)
	foutput.close()
	
def StrToNumList(s):
	#return [int(x) for x in re.findall('[0-9\-]+',s)]
	return [int(x) for x in s[:-1].split()]


def solve_lwm(M, N, A):
	m = min([min(line) for line in A])
	row_check_flags = [0]*M
	col_check_flags = [0]*N

	for i in range(M):
		for j in range(N):
			if A[i][j] == m:
				if row_check_flags[i] == 1 or m*N == sum(A[i]):
					row_check_flags[i] = 1
					continue
				elif col_check_flags[j] == 1 or m*M == sum([A[k][j] for k in range(M)]):
					col_check_flags[j] = 1
					continue
				else:
					return "NO"

	return "YES"
##########################################################################################################################
# Main code goes here
					
problem = 'b'
s_input = 'small'
s_id = 'lwm'

nCase, inputList = parseInputData(problem, s_input, s_id)
result = []
rownum = 0



for i in range(nCase):
	M, N = StrToNumList(inputList[rownum])
	A = [StrToNumList(line) for line in inputList[rownum + 1 : rownum + 1 + M]]
	result.append("Case #%d: %s\n" %(i+1, solve_lwm(M, N, A)))
	rownum += M + 1
writeOutput(result, problem, s_input, s_id)





			




		




		

