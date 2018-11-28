#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  problem1.py
#  
#  Copyright 2013 Dino <dino@Dracon>
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
	
	dat = open("A-large.in",'r')
	dat2 = open("Program1.out",'w')
	
	T = int(dat.readline())
	
	for i in range(T):
		#Input
		Matrix = [['.' for x in xrange(4)] for x in xrange(4)]
		for j in range(4):
			row = dat.readline()
			sign = list(row.strip())
			for k in range(len(sign)):
				Matrix[j][k] = sign[k] 
				print Matrix[j][k],
			print("")
		print("")
		dat.readline()
		
		#checking
		finish = True
		printed = False
		for j in range(4):
			sumaRed = 0
			sumaStupac = 0
			dijagonala1 = 0
			dijagonala2 = 0
			for k in range(4):
				if Matrix[j][k] == '.':
					finish = False
				if Matrix[j][k] == 'X':
					sumaRed += 1
				if Matrix[j][k] == 'O':
					sumaRed -= 1
				if Matrix[j][k] == 'T':
					sumaRed += 100
				if Matrix[k][j] == 'X':
					sumaStupac += 1
				if Matrix[k][j] == 'O':
					sumaStupac -= 1
				if Matrix[k][j] == 'T':
					sumaStupac += 100
				if Matrix[k][k] == 'X':
					dijagonala1 += 1
				if Matrix[k][k] == 'O':
					dijagonala1 -= 1
				if Matrix[k][k] == 'T':
					dijagonala1 += 100
				if Matrix[k][3-k] == 'X':
					dijagonala2 += 1
				if Matrix[k][3-k] == 'O':
					dijagonala2 -= 1
				if Matrix[k][3-k] == 'T':
					dijagonala2 += 100
			if not printed:
				if sumaRed == 4 or sumaRed == 103 or sumaStupac == 4 or sumaStupac == 103 or dijagonala1 == 4 or dijagonala1 == 103 or dijagonala2 == 4 or dijagonala2 == 103:
					dat2.write("Case #{}: X won\n".format(i+1))
					printed = True
				elif sumaRed == -4 or sumaRed == 97 or sumaStupac == -4 or sumaStupac == 97 or dijagonala1 == -4 or dijagonala1 == 97 or dijagonala2 == -4 or dijagonala2 == 97:
					dat2.write("Case #{}: O won\n".format(i+1))
					printed = True
		if not printed:
			if finish:
				dat2.write("Case #{}: Draw\n".format(i+1))
			else:
				dat2.write("Case #{}: Game has not completed\n".format(i+1))
		
	return 0

if __name__ == '__main__':
	main()

