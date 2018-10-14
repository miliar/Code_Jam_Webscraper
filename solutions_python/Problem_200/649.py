import os
import sys
import numpy as np


def is_tidy(num):
	return all(num[i] <= num[i+1] for i in xrange(len(num)-1))

#inp = open("input.in", "r")
#inp = open("B-small-attempt0.in", "r")
inp = open("B-large.in", "r")

#outp = open("output.out", "w")
#outp = open("B-small-attempt0.out", "w")
outp = open("B-large.out", "w")


T = int(inp.readline().rstrip())

for i in range(T):
	num = map(int, list(inp.readline().rstrip()))
	#print num

	if is_tidy(num):
		#print "Result : " + ''.join(map(str,num))
		outp.write("Case #" + str(i+1) + ": " + ''.join(map(str,num)) +"\n")

	else:
		rev_num = num[::-1]
		for ind in range(len(rev_num)):	
			if ind<len(num)-1:
				if rev_num[ind]<rev_num[ind+1]:
					for t in range(ind+1):
						rev_num[t] = 9
					rev_num[ind+1] -= 1
		
		num = rev_num[::-1]
		for d in range(len(num)):
			if num[d]==0:
				num = num[1:]
			else:
				break

		#print "Result : " + ''.join(map(str,num))
		outp.write("Case #" + str(i+1) + ": " + ''.join(map(str,num)) +"\n")

inp.close()
outp.close()
