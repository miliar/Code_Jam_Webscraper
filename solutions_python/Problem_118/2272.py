#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2013 Shiva Narrthine <shivanarrthine@betaas-Z68P-DS3>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  



def main():
	
	#read input file
	fin = open('C-small-attempt0.in','r')
	inputdata = fin.readlines()
	fin.close()
	
	
	it = iter(inputdata)
	
	#create output file
	fout = open('fsOutput-small.txt','w')
	
	#get values from input file
	testcases = int(it.next())
	#print  testcases
	
	for i in range(0,testcases):
		
		#get values from input file
		nums = [int(y) for y in it.next().split()]
		
		palindrome = 0
		
		for num in range(nums[0],nums[1]+1):
			
			
			# check for palindromes
			p1 = [int(a) for a in str(num)]
			l1 = len(str(num))
			
			if p1[0]==p1[l1-1]:
				
				# check if square
				num_sqrt = num**(1/2.0)
				if num_sqrt%1==0:
					num_sqrt = int(round(float(num_sqrt)*1))
					
					# check if square is a palindrome
					p2 = [int(b) for b in str(num_sqrt)]
					l2 = len(str(num_sqrt))
					
					if p2[0]==p2[l2-1]:
						palindrome+=1
						#print "p: " + str(num) + str(num_sqrt) + str(palindrome)
			
		#print "palindromes: " + str(palindrome)
		fout.write("Case #" + str(i+1) + ": " + str(palindrome) + "\n")
	return 0

if __name__ == '__main__':
	main()

