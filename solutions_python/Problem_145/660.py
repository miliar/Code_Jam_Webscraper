#! /usr/bin/env python
import math


#################################################################################################

def parseInputData(problem, s_input, s_id):
	finput = open(problem + '-' + s_input + '-' + s_id + '.in','r')
	nCase = int(finput.readline().strip())
	inputList = finput.readlines()	
	finput.close()
	return nCase, inputList

#################################################################################################

def writeOutput(result, problem, s_input, s_id):
	foutput = open(problem + '-' + s_input + '-' + s_id + '.out','w')
	foutput.writelines(result)
	foutput.close()
	
#################################################################################################

def StrToNumList(s):
	s = s.strip()
	return [int(x) for x in s.split()]

def StrToNum(s):
	return int(s.strip())

def StrToNum(s):
	return int(s.strip())

#################################################################################################


def solve_elf(f):
	p, q = f.strip().split('/')
	p = int(p)
	q = int(q)
	# print "new case" , p, q
	
	if q % p == 0:
		q = q/p
		p = 1

	if math.log(q, 2) % 1 != 0:
		return "impossible"

	q = q/2
	count = 1
	# print p, q
	while ((1.0*p)/q) < 1:
		count += 1
		q = q/2
		if q == 0:
			break
		# print p, q

	return str(count)




	

###################################################################################################
					
problem = 'A'
s_input = 'small'
s_id = 'elf'

nCase, inputList = parseInputData(problem, s_input, s_id)
result = []
# rownum = 0

for i in range(nCase):
	# n = 0 
	result.append("Case #%d: %s\n" %(i+1, solve_elf(inputList[i])))
	# rownum += n + 1
	
writeOutput(result, problem, s_input, s_id)



		




		

