#!/usr/bin/python
# -*- coding: utf-8 -*-


def doit():
	input = open("A.in", 'r')
	output = open("A.out", 'w')
	T = int( input.readline() )
	
	i = 0
	while i < T:
		line = input.readline().split()
		N = int( line[0] )
		prog = []
		
		j = 0
		while j < N:
			prog.append(   (  line[2*j+1], int( line[2*j+2] )  )   )
			
			j = j+1
		
		val = compute( prog )
		
		output.write( "Case #"+str(i+1)+": "+str(val)+"\n" )
		
		i = i+1
	
	output.close()
	input.close()


def compute( prog ):
	counter = 0
	
	# First is Blue, second is Orange
	pos = { 'B': 1, 'O': 1 }
	free = { 'B': 0, 'O': 0 }
	
	for i in prog:
		time = abs( i[1] - pos[ i[0] ] ) + 1
		time = max( 1, time-free[ i[0] ] )
		
		pos[ i[0] ] = i[1]
		
		for j in free.keys():
			if j != i[0]:
				free[j] = free[j] + time
			else:
				free[j] = 0
		
		counter = counter + time
	
	return counter


doit()
