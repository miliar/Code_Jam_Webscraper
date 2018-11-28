#!/usr/bin/python
# -*- coding: latin-1 -*-
from math import floor

inp = open('C.in')
out = open('C.out','w')


cases = int(inp.readline())
for case in xrange(cases):
	done = []
	line = inp.readline()
	numbers = line.split(' ')
	possibilities = 0
	if len(numbers[0]) == 0:
		out.write("Case #"+str(case+1)+": 0")
	else:
		for num in xrange(int(numbers[0]),int(numbers[1])):
			num = str(num)
			for char in xrange(1,len(num)):
				shifted = num[char:]+num[:char]
				pair = (min(num,shifted),max(num,shifted))
				if  not (pair in done or num == shifted) and int(shifted) in range(int(numbers[0]),int(numbers[1]) + 1 ):
					done.append(pair)
					possibilities +=1
					
	
	out.write("Case #"+str(case+1)+": "+str(possibilities)+"\n")