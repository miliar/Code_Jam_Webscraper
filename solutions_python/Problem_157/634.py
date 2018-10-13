#!/usr/bin/env python
# -*- coding: utf-8 -*-

def mult(a, b):
	t = {
	'1': {'1': '1', 'i': 'i', 'j': 'j', 'k': 'k'},
	'i': {'1': 'i' , 'i': '-1', 'j': 'k', 'k': '-j'},
	'j': {'1': 'j' , 'i': '-k', 'j': '-1', 'k': 'i'},
	'k': {'1': 'k' , 'i': 'j', 'j': '-i', 'k': '-1'},
	}
	sign = 1
	if len(a) == 2:
		sign *= -1
	if len(b) == 2:
		sign *= -1
	a = a.replace('-', '')	
	b = b.replace('-', '')
	res = t[a][b]
	if len(res) == 2:
		sign *= -1
	return res.replace('-', '') if sign > 0 else '-' + res.replace('-', '')
def test_s(s):
	z = s[0]
	i = 0
	while i < len(s): 		
		i +=1
		if i < len(s):
			z = mult(z, s[i])
	return z
def solve(L, X, S):
	I = X * S
	c = I[0]
	i = 0
	stage = ['i', 'j', 'k']
	stage_i = 0 
	while i < len(I) :
		if c == stage[stage_i]:
			stage_i += 1				
			#print I[i+ 1:], stage_i
			if stage_i == 3:
				if i == len(I) - 1:
					return 'YES'
				else:					
					if test_s(I[i+1:]) == '1':
						return 'YES'
					else:
						return 'NO'
			c = '1'			
		i += 1
		if i < len(I):
			c = mult(c, I[i])
	return 'NO'
if __name__ == "__main__":
	#print test_s('jijiji')
	testcases = input() 
	for caseNr in xrange(1, testcases+1):
		[L,X] = raw_input().split(" ")
		L = int(L)
		X= int(X)
		S = raw_input()
		
		print("Case #%i: %s" % (caseNr, solve(L, X, S)))
