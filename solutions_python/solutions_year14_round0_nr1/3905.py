#!/usr/bin/python
# -*- coding: utf-8 -*-

file = open("A-small-attempt2.in").readlines()
f = open('result','w')
counter = 1
for i in range(1,len(file)):
	idx = i%5
	if idx == 1:
		if i % 10 == 1:
			x = set(file[i+int(file[i])].strip().split(' '))
		else:
			y = set(file[i+int(file[i])].strip().split(' '))
			result = len( x & y )
			if result == 1:
				f.write('Case #'+str(counter)+': '+(x & y).pop()+'\n')
			elif result > 1:
				f.write('Case #'+str(counter)+': Bad magician!\n')
			elif result == 0:
				f.write('Case #'+str(counter)+': Volunteer cheated!\n')
			counter = counter + 1
		pass
f.close()
