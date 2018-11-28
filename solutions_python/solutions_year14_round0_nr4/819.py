#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Question 2.py
#  
#  Copyright 2014 Srinivasan <srinivasan@srinivasan-Dell-System-Inspiron-N4110>

def war():
	ans1 = []
	ans2 = []
	count = 0
	count2 = 0
	temp = raw_input()
	temp = temp.split(" ")
	for i in temp:
		ans1.append(float(i))
	temp = raw_input()
	temp = temp.split(" ") 
	for i in temp:
		ans2.append(float(i))
	ans1.sort()
	ans2.sort()
	a1 = ans1[:]
	a2 = ans2[:]
	while(a1 != []):
		if(a1[0] > a2[0]):
			a1 = a1[1:]
			a2 = a2[1:]
			count2 += 1
		else:
			a2.pop()
			a1 = a1[1:]
				
	while(ans1 != []):
		if(ans1.pop() > ans2[-1]):
			ans2 = ans2[1:]
			count += 1
		else:
			ans2.pop()
	return count2, count
	

if __name__ == '__main__':
	pass
	x = input()
	for i in range(x):
		input()
		temp = "Case #"
		temp += (str(i+1) + ":")
		w = war()
		print temp, w[0], w[1]
