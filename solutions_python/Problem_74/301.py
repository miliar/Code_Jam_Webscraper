#!/usr/bin/env python
# encoding: utf-8

import sys
import os

def moveCloser(curr,target):
	if target > curr:
		return curr + 1
	else:
		return curr - 1

def solveSingle(lines):
	
	B = []
	O = []
	o_pos = 1
	b_pos = 1
	secs = 0
	
	for x in range(0,len(lines),2):
		if lines[x] == 'O':
			O.append(int(lines[x+1]))
		else:
			B.append(int(lines[x+1]))
	
	i = max([len(O),len(B)]);
	
	while B != [] or O != []:
		
		if O == []:
			if b_pos == B[0]:
				B = B[1:]
				lines = lines[2:]
			else:
				b_pos = moveCloser(b_pos,B[0])
		
		elif B == []:
			if o_pos == O[0]:
				O = O[1:]
				lines = lines[2:]
			else:
				o_pos = moveCloser(o_pos,O[0])
				
		elif b_pos == B[0] and o_pos == O[0]:
			if(lines[0] == 'B'):
				lines = lines[2:]
				B =B[1:]
			
			elif(lines[0] == 'O'):
				lines = lines[2:]
				O = O[1:]
		
		elif b_pos == B[0]:
			if(lines[0] == 'B'):
				lines = lines[2:]
				B = B[1:]
		
			o_pos = moveCloser(o_pos,O[0])
		
		elif o_pos == O[0]:
			if(lines[0] == 'O'):
				lines = lines[2:]
				O = O[1:]
			
			b_pos = moveCloser(b_pos,B[0])
		
		else:
			b_pos = moveCloser(b_pos,B[0])
			o_pos = moveCloser(o_pos,O[0])
		
		secs += 1
	
	return secs
			
			

def main():
	infile = open('A-large.txt','r')
	outfile = open('A-large-answer.txt','w')
	num_tests = int(infile.readline())
	
	for x in range(num_tests):
		lines = infile.readline().split(" ")
		lines = lines[1:]
		lines = [l.strip() for l in lines]
	
		secs = solveSingle(lines)
	
		outfile.write("Case #"+str(x+1)+": "+str(secs)+"\n")
		print "Case #"+str(x+1)+": "+str(secs)
	
	
	infile.close()
	outfile.close()


if __name__ == '__main__':
	main()

