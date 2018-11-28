#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Alberto Barrionuevo Castillo on 2011-05-07.
Copyright (c) 2011 Darko. All rights reserved.
"""
import string

f = open('A-large.in')
aux = f.readline()
for i in range(0, int(aux)):
	aux = f.readline().strip().partition(' ')
	pos = {'O' : 1, 'B': 1 }
	timer = {'O' : 0, 'B': 0 }
	time = 0
	for j in range(0, int(aux[0])):
		aux = str(aux[2])
		aux = aux.partition(' ')
		robot = aux[0]
		aux = str(aux[2])
		aux = aux.partition(' ')
		mov = int(aux[0])
		inc = abs(mov - pos[robot]) - (time - timer[robot])
		# print 'robot:%s, mov:%d, inc:%d' % (robot, mov, inc)
		if inc < 0:
			time += 1
			pos[robot] = mov
			timer[robot] = time
		else:
			time = time + inc + 1
			pos[robot] = mov
			timer[robot] = time
	print 'Case #%s: %d' % (i+1, time)