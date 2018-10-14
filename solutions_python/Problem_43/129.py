#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

def doit():
	input = open("A.in", 'r')
	output = open("A.out", 'w')
	
	T = int( input.readline().strip() )
	
	i = 1
	
	while i <= T:
		avail = []
		dict = [1,0]
		num = []
		tmp = input.read(1)
		val = 0L
		
		while tmp != '\n':
			num.append( tmp )
			
			exists = False
			
			for j in avail:
				if j == tmp:
					exists = True
					break
			
			if exists == False:
				avail.append( tmp )
			
			tmp = input.read(1)
		
		j = 2
		
		while j < len( avail ):
			dict.append( j )
			
			j = j+1
		
		j = 0
		b = len( dict )
		
		while j < len( num ):
			#print num[len(num)-1-j]
			val = val + long(  dict[  avail.index( num[len(num)-1-j] )  ] * math.pow( b, j )  )
			
			j = j+1
		
		output.write("Case #" + str(i) + ": " + str( val ) + "\n" )
		
		i = i+1
	
	output.close()
	input.close()



doit()
