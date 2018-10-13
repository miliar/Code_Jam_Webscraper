#!/usr/bin/python
# -*- coding: utf-8 -*-


def doit():
	input = open("B.in", 'r')
	output = open("B.out", 'w')
	
	T = int( input.readline().strip() )
	
	i = 1
	
	while i <= T:
		num = []
		tmp = input.read(1)
		
		while tmp != '\n':
			num.append( int(tmp) )
			tmp = input.read(1)
		
		#print num
		
		output.write("Case #" + str(i) + ": " + outputify(  next( num )  ) + "\n" )
		
		i = i+1
	
	output.close()
	input.close()



def next( digits ):
	smallest_i = len( digits )
	smallest_v = 10
	
	i = len( digits )-2
	
	done = False
	
	while i >= 0:
		if digits[i] < digits[i+1]:
			j = i
			
			while j < len( digits ):
				if digits[j] > digits[i] and digits[j] < smallest_v:
					smallest_v = digits[j]
					smallest_i = j
				
				j = j+1
			
			swap = digits[i]
			digits[i] = smallest_v
			digits[ smallest_i ] = swap
			
			digits = minimize( digits, i )
			
			done = True
			break
		
		i = i-1
	
	if done == False:
		digits.sort()
		
		digits.insert( 0, 0 )
		
		digits = normalize( digits )
	
	#print digits
	
	return digits


def minimize( digits, start ):
	end = digits[ start+1:len( digits ) ]
	
	end.sort()
	
	#print end
	
	i = 0
	
	while i < len( end ):
		digits[ start+1+i ] = end[ i ]
		
		i = i+1
	
	return digits


def normalize( digits ):
	i = 0
	
	while i < len( digits ):
		if digits[i] != 0:
			swap = digits[i]
			digits[i] = 0
			digits[0] = swap
			
			break
		
		i = i+1
	
	return digits


def outputify( list ):
	result = ""
	
	for i in list:
		result = result + str( i )
	
	return result


doit()
