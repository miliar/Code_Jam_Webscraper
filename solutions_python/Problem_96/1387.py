#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
def r():
	for line in sys.stdin:
		for tok in line.strip().split():
			yield tok
inp = r()

def bestResultHigherThan(p, num):
	a = num / 3;
	b = num % 3;
	c = a + (0 if(b == 0) else 1)
	if(c>=p): return 'yes'
	if(p-c==1 and (b==0 or b==2) and c!=0):
		return 'surprise'
	return 'no'

t = int(inp.next())
for cases in range(1,t+1):
	n = int(inp.next())
	s = int(inp.next())
	p = int(inp.next())
	t = []
	yes = 0
	surprise = 0	
	for i in range(n):
		num = int(inp.next())
		t.append(num)
		v = bestResultHigherThan(p, num)
		if(v == 'yes'): yes += 1
		elif(v == 'surprise'): surprise += 1
	total = yes + (s if(surprise>s) else surprise)	
	print 'Case #' + str(cases) + ': ' + str(total)
	
