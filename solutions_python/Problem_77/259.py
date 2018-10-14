#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

def doit():
	input = open("D.in", 'r')
	output = open("D.out", 'w')
	T = int( input.readline() )
	
	i = 0
	while i < T:
		N = int( input.readline() )
		line = input.readline().split()
		values = []
		
		for j in line:
			values.append( int(j) )
		
		#print values
		out = compute( values )
		
		output.write( "Case #"+str(i+1)+": "+out+"\n" )
		
		i = i+1
	
	output.close()
	input.close()


def compute( values ):
	out = 0
	done = []
	
	while len(done) != len(values):
		cycle = []
		
		for i in values:
			if not i-1 in done:
				init = i-1
				break
		
		v = init
		start = True
		while v != init or start:
			start = False
			cycle.append( v )
			v = values[ v ]-1
		
		done.extend( cycle )
		
		if len( cycle ) != 1:
			out = out+len( cycle )
	
	return str( "%.6f" % out )


doit()
