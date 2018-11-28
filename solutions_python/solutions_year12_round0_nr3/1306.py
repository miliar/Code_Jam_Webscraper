# Google Code jam Problem C Recycled Numbers
# Apr. 13, 2012
# Python 3.2.3

import sys
import string

def Combine(n):
	if n <= 1:
		return 0;

	if (n == 2):
	    return 1
	
	return n*(n-1)/2

def Normalize(s, l):
	if (l <= 1):
		return s

	smallest = int(s[0])
	#pos = 0

	for i in range(l):
		if int(s[i]) < smallest:
			smallest = int(s[i])
	#		pos = i

	#if (pos == 0):
	#	return s
	
	#a = s[pos:] + s[:pos]
	#print(a)

	#process cases: 1291 -> 1129; 33533 -> 33335, 813611 _> 136118 (not 118136)
	#preserve 1111-> 1111 33534-> 33534

	candidate = int(s)

	for i in range(l):
		if (int(s[i]) == smallest):
			tmp = s[i:] + s[:i]
			if (int(tmp) < candidate):
				candidate = int(tmp)

	return str(candidate)
	
#	pos = l
#	found_end = False
#
#	for i in range(len(a)-1, -1, -1):
#		if (int(a[i]) == smallest):
#			pos = i;
#			found_end = True
#		else:
#			found_end = False
#
#		if not found_end:
#		    break
#	
#	if (pos > 0 & pos < l):
#		a = a[pos:] + a[:pos]
#
#	return a

def main(inFileName):
   inFile = open(inFileName, mode='r')
   
   numberOfCases = int(inFile.readline())

   #print(Normalize(str(141), len(str(141))))
   
   for caseNumber in range(numberOfCases):
	   line = inFile.readline().split()
	   a = (int)(line[0])
	   b = (int)(line[1])
	   word_len = len(str(a))

	   answer = 0
	   d = {}

	   if word_len <= 1:
		   print('Case #' + str(caseNumber+1) + ': ' + str(answer) )
		   continue

	   for i in range(a, b+1):
		   nor = Normalize(str(i), word_len)
		   #print( str(i) + ":" + nor)
		   if (nor in d):
			   d[nor] += 1
		   else:
			   d[nor] = 1

	   for (k, v) in sorted(d.items()):
		   answer += Combine(int(v))
		   #print(k + ":" + str(v) + ":" + str(Combine(int(v))))

	   print('Case #' + str(caseNumber+1) + ': ' + str(int(answer)) )
   
if __name__ == '__main__': 
   main(sys.argv[1])
