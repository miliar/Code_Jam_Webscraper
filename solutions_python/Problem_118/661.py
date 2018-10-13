# Javier Fernandez Google Code Jam 2013
# Google Code Jam 2013
# javierfdr@gmail.com - javierfdr

# This file allows to generate a python array containing the fair palindrome numbers until N

import sys
import time
import math

def generate_palindrome_int_sqrt(n):
	l = []
	c = 0
	imp = 1 
	t = time.time()
	while c<=n:
		c = c+imp
		imp = imp+2

		if c<=n:
			if is_palindrome(c):
				sqrt = math.sqrt(c)
				if is_palindrome(int(sqrt)):				
					l.append(c)
	
	print time.time()-t
	return l

def is_palindrome(n):
	i = str(n)
	init = 0
	end = len(i)-1

	while(init<end):
		if(i[init]!=i[end]):
			return False
		init = init+1
		end = end-1
	return True

out_file = open('gen.out','w+')
n = 1000000000000000
l = generate_palindrome_int_sqrt(n)
a = 'fairpal=['
for i in l:
	a = a+''+str(i)+','
a = a.rstrip(',')
a = a + ']'
out_file.write(a)


#in_file = sys.stdin
#num_cases = int(in_file.readline())
#g = generate_fair_palindromes(1001)
#for c in range(1,num_cases+1):
#	case = 'Case #'+str(c)+': '
#	ab= in_file.readline().strip('\n').split()
#	r = palindromes_bet(g,int(ab[0]),int(ab[1]))

#	result = case+str(r)+'\n'
#	out_file.write(result)