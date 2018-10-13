#! /usr/bin/env python
import sys
import math

def is_square_of_palindrome(num):
	sq = math.sqrt(num)
	return sq == int(sq) and is_palindrome(int(sq))
	
def is_palindrome(num):
	w = str(num)
    	return w == w[::-1]

def process_input():
	sets = int(sys.stdin.readline())
	for s in range(sets):
		nums = sys.stdin.readline().strip().split()
		A = int(nums[0])
		B = int(nums[1])+1
		valid = 0
		for i in range(A,B):
			if (is_palindrome(i) and is_square_of_palindrome(i)):
				valid+=1
		
		print 'Case #'+str(s+1)+': '+str(valid)


process_input()
