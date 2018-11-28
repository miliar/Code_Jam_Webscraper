'''

	Case #1: 2
	Case #2: 0
	Case #3: 2
    

'''

import os
import sys
import pdb
import math
from os.path import basename

sqr_hash = {}

def checkPalindrome(n):
	s = ""
	if n <=9 and n>=1:
		return 1
	elif n > 9:
		s = str(n)
	
	i=0
	j=len(s)-1
	while i<=j:
		if s[i] == s[j]:
			i+=1
			j-=1
		else:
			return 0
	return 1		
	

def getResult(fo, mlist, index):
	fair_count=0
	x = mlist[index].split()
	s = int(x[0])
	e = int(x[1])   
	s_i=0 
	e_i=0
	if s < 1 or e > 1000 or s > e:
		print "Out of bound index error" 
		return
	start_flag = 0
	end_flag = 0
	
	s_sqrt = int(math.sqrt(s))
	if s == int(math.pow(s_sqrt,2)):
		start_flag = 1
		
	e_sqrt = int(math.sqrt(e))
	if e == int(math.pow(e_sqrt,2)):
		end_flag = 1
	
	if start_flag == 1:
		s_i = s_sqrt
	else:
		s_i = s_sqrt+1

	if end_flag == 1:
		e_i = e_sqrt
	else:
		e_i = e_sqrt+1
	
	for i in range(s_i,e_i+1):
		t = int(math.pow(i,2))
		if t<=e and t>=s and checkPalindrome(i) and checkPalindrome(t):
			#print i, t
			fair_count+=1
	fo.write("Case #"+str(index)+": "+str(fair_count)+"\n")	
	return


if __name__ == "__main__":
	if len(sys.argv) != 2:
		sys.exit()
	
with open(sys.argv[1], 'r') as f:
	read_data = f.readlines()	

fo = open(os.path.splitext(basename(sys.argv[1]))[0]+".out", 'w')
# Extract test_case
test_case = int(read_data[0])


if test_case > 100 or test_case < 1:
	sys.exit()

#print read_data, test_case
#pdb.set_trace()
for i in range(test_case):
	getResult(fo,read_data, i+1)

f.close()
fo.close()
	
	



