#!/usr/bin/python
from math import sqrt,ceil,floor;
filename = "sample.in";
filename = "C-small-attempt0.in";
#filename = "C-large.in";
def isAnagram(n):
	myStr = str(n);
	i = 0;
	j = len(myStr)-1;
	while(i < j):
		if myStr[i] != myStr[j]:
			return False
		i+=1;
		j-=1;
	return True;
data_sets = [map(int,line.strip().split()) for line in open(filename,'r').readlines()[1:]]
i = 0;
case = 1;
for data_set in data_sets:
	minSquareRoot = int(ceil(sqrt(data_set[0])));
	maxSquareRoot = int(floor(sqrt(data_set[1])));
	countAnagrams = 0;
	for i in xrange(minSquareRoot, maxSquareRoot+1):
		if(isAnagram(i)):
			squared = i*i;
			if(isAnagram(squared)):
				countAnagrams += 1;
	caseString = str(countAnagrams);
	print "Case #" + str(case) + ": " + caseString;
	case+=1;
	
