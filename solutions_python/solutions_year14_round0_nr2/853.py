#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Question 2.py
#  
#  Copyright 2014 Srinivasan <srinivasan@srinivasan-Dell-System-Inspiron-N4110>

def cookie():
	ans1 = raw_input()
	ans1 = ans1.split(" ")
	c = float(ans1[0])
	f = float(ans1[1])
	x = float(ans1[2])
	count = 0.0
	factor = 2.0
	balance = 0.0
	while(balance < x):
		temp1 = (x - balance ) / factor
		temp2 = -1
		if(balance >= c):
			temp2 = (x - (balance - c) ) / (factor + f)
		
		if(temp2 == -1 and x < c):
			count += (x - balance ) / factor
			balance = x
		elif(temp2 == -1 and x > c):
			count += (c - balance ) / factor
			balance = c
		elif(temp2 != -1 and temp1 <= temp2):
			count += temp1
			balance = x
		else:
			balance -= c
			factor += f
			
	return count
	

if __name__ == '__main__':
	pass
	x = input()
	for i in range(x):
		temp = "Case #"
		temp += (str(i+1) + ":")
		print temp,'%.7f' %cookie()

