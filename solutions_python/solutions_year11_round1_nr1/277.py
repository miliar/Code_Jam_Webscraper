#!/usr/bin/env python
# encoding: utf-8


import sys
import os


def processRow(n,pd,pg):
	
	if pd < 100 and pg == 100:
		return "Broken"
	
	if pd > 0 and pg == 0:
		return "Broken"
	
	if pd == 0:
		return "Possible"
	
	found = False
	
	for x in range(1,n+1):
		check = float(pd/100.0)*float(x)
		if (abs(check - int(check)) < 1e-8):
			found = True
			break

	if found:
		return "Possible"
	else:
		return "Broken"
			

def main():
	infile = open('A-small.txt','r')
	outfile = open('A-small-answer.txt','w')
	
	num_tests = int(infile.readline())

	for x in range(num_tests):
		nums = infile.readline().split()
		nums = [int(n.strip()) for n in nums]
		
		answer = processRow(nums[0],nums[1],nums[2])
		
		print "Case #"+str(x+1)+":",answer
		outfile.write("Case #"+str(x+1)+": "+str(answer)+"\n")

	
	infile.close()
	outfile.close()


if __name__ == '__main__':
	main()

