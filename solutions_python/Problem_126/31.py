from math import *;
INPUT_NAME = 'A-large.in'
OUTPUT_NAME = 'A-large.out'
#INPUT_NAME = 'A-small-attempt1.in'
#OUTPUT_NAME = 'A-small-1.out'

#INPUT_NAME = 'A.in'
#OUTPUT_NAME = 'A.out'
	
def solve(S, n):		
	#print S, n
	pp1 = 0
	nr = 0
	total = 0
	N = len(S)
	for i in xrange(N):
		if S[i]==1:
			nr += 1
			if(nr >= n):				
				total += (i-n-pp1+2)*(N-i)					
				#print pp1, (i-n-pp1+2), (N-i)									
				pp1 = i-n+2					
		else:
			nr = 0
	return total
 
	
##### THIS IS THE "MAIN" FUNCTION #####
def fullsol(slst):
	T = int(slst[0]) # number of test cases
	sol = [];
	cur = 1;
	for i in xrange(T):	
		x = slst[cur].split()
		S = [0 if i in ('a', 'e', 'i', 'o', 'u') else 1 for i in x[0]]
		n = int(x[1])		
		sol.append(solve(S, n))
		cur += 1
	return sol
##### ############################### ######
	
# UTILITY FUNCTIONS	
def makestring(row):
	# make a list into a string separated by spaces
	return ''.join([' '+str(i) for i in row])[1:]

def olwrite(fname, answers):
	# write outputs to file line by line [one-line outputs]
	f = open(fname, 'w')
	lines = ['Case #'+str(i+1)+': '+str(answers[i])+'\n' for i in xrange(len(answers))]
	f.writelines(lines)
	f.close()
	return
	
def sread(fname):
	f = open(fname, 'r')
	res = [x.strip() for x in f.readlines()]
	f.close()
	return res
	
stuff = sread(INPUT_NAME)
answers = fullsol(stuff)
olwrite(OUTPUT_NAME, answers)


	