#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Question 1.py
#  
#  Copyright 2014 Srinivasan <srinivasan@srinivasan-Dell-System-Inspiron-N4110>

def magician():
	ans1 = input()
	ls1 = []
	for i in range(4):
		temp = raw_input()
		temp = temp.split(" ")
		for i in temp:
			ls1.append(int(i))
	
	ans2 = input()
	ls2 = []
	for i in range(4):
		temp = raw_input()
		temp = temp.split(" ")
		for i in temp:
			ls2.append(int(i))
	
	ans1 -= 1
	ans2 -= 1
	
	val1 = []
	i = ans1*4
	while(i < ((ans1*4) + 4)):
		val1.append(ls1[i])
		i+=1
		
	val2 = []
	i = ans2*4
	while(i < ((ans2*4) + 4)):
		val2.append(ls2[i])
		i+=1
	
	count = "Volunteer cheated!"
	for i in val1:
		for j in val2:
			if count == "Volunteer cheated!" and i == j:
				count = i
			elif i == j:
				count = "Bad magician!"

	return count
	

if __name__ == '__main__':
	pass
	x = input()
	for i in range(x):
		temp = "Case #"
		temp += (str(i+1) + ": ")
		print temp,magician()

