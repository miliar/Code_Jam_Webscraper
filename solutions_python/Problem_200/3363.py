#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 08:31:09 2017

@author: ska
"""
def tidy(m):
	s = str(m)
	k =len(s)
	for j in range(1,len(s)):
		if s[j]< s[j-1]:
#			print(j)
			k =j
			return False,k
	return True,k
		

for i in range(1,int(input())+1):
	n = int(input())
	s =str(n)
	boo, c = tidy(n)
	if boo:
		print("Case #{}: {}".format(i,n))
	else:
		while not boo:
#			print(s[c:])
			n = n-int(s[c:])-1
			s = str(n)
			
#			print(n)
			boo,c = tidy(n)
		print("Case #{}: {}".format(i,n))
			