#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

L = 0
words = []
regs = []

def parse():
	input = open("A.in", 'r')
	vals = input.readline().split()
	
	L = int( vals[0] )
	D = int( vals[1] )
	N = int( vals[2] )
	
	while D > 0:
		words.append( input.readline().strip() )
		D = D-1
	
	while N > 0:
		regs.append( input.readline().strip() )
		N = N-1
	
	input.close()


def doit():
	output = open("A.out", 'w')
	
	i = 1
	
	for case in regs:
		match = 0
		reg = re.compile( case.replace("(","[").replace(")","]") )
		
		for word in words:
			if reg.search( word ):
				match = match+1
		
		output.write("Case #" + str(i) + ": " + str(match) +"\n" )
		
		i = i+1
	
	output.close()


parse()
doit()
