# Run in command line
# E:\python27\python_nopause.bat B.py < "B-test.in" > "B-test-out.txt" 2>&1
# E:\python27\python_nopause.bat B.py < "B-small-attempt4.in" > "B-small-out.txt" 2>&1
# E:\python27\python_nopause.bat B.py < "B-large.in" > "B-large-out.txt" 2>&1

def checkdigit(x,out):
	# check if the list is sorted
	sval = all(x[i] <= x[i+1] for i in xrange(len(x)-1))
	if len(x) == 1:
		if out == []:
			return x
		elif out != []:
			return out+x
	elif sum(x) >= x[0]*len(x) and x[0]<=x[1]:
		# print sval
		out.append(x.pop(0))
		# print out, x
		return checkdigit(x,out)
	else:
		# print sval
		# print x, out
		if x[0]-1 == 0:
			res = [9]*(len(x)-1)			
			return res
		elif x[0]-1 > 0:
			if x[0]<x[1]:
				out.append(x.pop(0))
				# print out, x
				return checkdigit(x,out)
			else:
				res = [x[0]-1] + [9]*(len(x)-1)						
				return out+res
		
import os
from sys import *

T = int(stdin.readline())
for t in xrange(T):
	num = int(stdin.readline())
	num = [int(x) for x in str(num)]
	out = []
	res = "".join(str(x) for x in checkdigit(num, out)	)
	# for i in xrange(5):
		# print i
		# out = []
		# num = checkdigit(num, out)
	res = "".join(str(x) for x in checkdigit(num, out)	)
	print "Case #%s:" %(t+1), res