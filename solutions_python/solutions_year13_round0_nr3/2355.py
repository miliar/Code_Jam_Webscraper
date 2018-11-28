#!/usr/bin/python
import sys
import re
import math

T=int(sys.stdin.readline())
#print T

for i in range(1,T+1):
	res=re.findall('\d+', sys.stdin.readline())
	count=0
	for j in range(int(res[0]), int(res[1])+1):
		s1 = str(j)
		s2 = s1[::-1]
		if (s1 == s2):
			sq1 = j**(0.5)
			if(math.floor(sq1) == sq1):
				#print 'int!'
				sq1 = str(int(sq1))
				sq2 = sq1[::-1]
				if (sq1 == sq2):
					count = count+1
	
	print 'Case #'+str(i)+': '+str(count)


