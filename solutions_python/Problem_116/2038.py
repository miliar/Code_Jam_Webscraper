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
	fin = open('A-large.in','r')
	inputdata = fin.readlines()
	fin.close()
	
	# get rid of blank lines
	n_inputdata = []
	for line in inputdata:
		if not line.strip():
			continue
		else:
			n_inputdata.append(line)
	
	it = iter(n_inputdata)
	
	#create output file
	fout = open('ttttOutput-large.txt','w')
	
	#get values from input file
	testcases = int(it.next())
	print  testcases
	for i in range(testcases):
		
		# declaring winning check
		won = 0
		
		# get rows from input file
		row = []
		for j in range(4):
			row.append([str(y) for y in it.next()])
		'''
		row_1 = [str(y) for y in it.next()]
		row_2 = [str(y) for y in it.next()]
		row_3 = [str(y) for y in it.next()]
		row_4 = [str(y) for y in it.next()]
		'''
		
		print "case: " + str(i+1) 
		# horizontal checks
		for r in row:
			# check for X horizontally
			check1 = 0	
			for box in r:
				if box=='X' or box=='T':
					if check1==3:
						print "X Won"
						won = 1
					check1 +=1
					continue
				else:
					break 
		
			# check for Y horizontally
			check1 = 0	
			for box in r:
				if box=='O' or box=='T':
					if check1==3:
						print "O Won"
						won = 2
					check1 +=1
					continue
				else:
					break 
					
		# store values in vertical rows
		v1 = []
		v2 = []
		v3 = []
		v4 = []
		for r in row:
			
			v1.append(r[0])
			v2.append(r[1])
			v3.append(r[2])
			v4.append(r[3])
			
		
		#vertical checks
		
		#v1 x
		check1 = 0
		for box in v1:
			if box=='X' or box=='T':
				if check1==3:
					print "X Won"
					won = 1
				check1+=1
				continue
			else:
				break
		
		#v2 x
		check1 = 0
		for box in v2:
			if box=='X' or box=='T':
				if check1==3:
					print "X Won"
					won = 1
				check1+=1
				continue
			else:
				break
				
		#v3 x
		check1 = 0
		for box in v3:
			if box=='X' or box=='T':
				if check1==3:
					print "X Won"
					won = 1
				check1+=1
				continue
			else:
				break
				
		#v4 x
		check1 = 0
		for box in v4:
			if box=='X' or box=='T':
				if check1==3:
					print "X Won"
					won = 1
				check1+=1
				continue
			else:
				break	
		
		#v1 o
		check1 = 0
		for box in v1:
			if box=='O' or box=='T':
				if check1==3:
					print "O Won"
					won = 2
				check1+=1
				continue
			else:
				break
		
		#v2 O
		check1 = 0
		for box in v2:
			if box=='O' or box=='T':
				if check1==3:
					print "O Won"
					won = 2
				check1+=1
				continue
			else:
				break
				
		#v3 O
		check1 = 0
		for box in v3:
			if box=='O' or box=='T':
				if check1==3:
					print "O Won"
					won = 2
				check1+=1
				continue
			else:
				break
				
		#v4 x
		check1 = 0
		for box in v4:
			if box=='O' or box=='T':
				if check1==3:
					print "O Won"
					won= 2
				check1+=1
				continue
			else:
				break	
		
		# Diagonal checks 
		# foward slash, X
		if v1[0]=='X' or v1[0]=='T':
			if v2[1]=='X' or v2[1]=='T':
				if v3[2]=='X' or v3[2]=='T':
					if v4[3]=='X' or v4[3]=='T':
						print "X won"
						won = 1
		
		# backward slash, X
		if v1[3]=='X' or v1[3]=='T':
			if v2[2]=='X' or v2[2]=='T':
				if v3[1]=='X' or v3[1]=='T':
					if v4[0]=='X' or v4[0]=='T':
						print "X won"
						won = 1
						
		# foward slash, O
		if v1[0]=='O' or v1[0]=='T':
			if v2[1]=='O' or v2[1]=='T':
				if v3[2]=='O' or v3[2]=='T':
					if v4[3]=='O' or v4[3]=='T':
						print "O won"
						won = 2
		
		# backward slash, O
		if v1[3]=='O' or v1[3]=='T':
			if v2[2]=='O' or v2[2]=='T':
				if v3[1]=='O' or v3[1]=='T':
					if v4[0]=='O' or v4[0]=='T':
						print "O won"
						won = 2
		
		# Detect draws
		draw  = 1
		if won==0:
			for r in row:
				for box in r:
					if box=='.':
						draw = 0
			if draw==0:
				fout.write("Case #" + str(i+1) + ": Game has not completed\n")
			else:
				fout.write("Case #" + str(i+1) + ": Draw\n")
		elif won==1:
			fout.write("Case #" + str(i+1) + ": X won\n")
		elif won==2:
			fout.write("Case #" + str(i+1) + ": O won\n")
			
				
	
	return 0

if __name__ == '__main__':
	main()

