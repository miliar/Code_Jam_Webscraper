#!/usr/bin/python
# -*- coding: utf-8 -*-


def doit():
	input = open("C.in", 'r')
	output = open("C.out", 'w')
	
	string = "welcome to code jam"
	mod = 10000
	
	N = int( input.readline().strip() )
	
	print N
	
	i = 1
	
	while i <= N:
		line = input.readline().strip()
		
		output.write("Case #" + str(i) + ": " + str(  findall2( string, line, mod )  ).rjust(4, '0') +"\n" )
		
		i = i+1
	
	output.close()
	input.close()


def findall2( pattern, string, mod ):
	if len( pattern ) == 1:
		return string.count( pattern[0] )
	
	ret = 0
	start = string.find( pattern[0] )	
	
	while start >= 0 and start < len( string ):
		start = start+1
		
		ret = ( ret + findall2( pattern[1:], string[start:], mod )  ) % mod
		
		start = string.find( pattern[0], start )
	
	return ret


doit()
