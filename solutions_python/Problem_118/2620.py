#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  problem2.py
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

import math

def isPalindrom(broj):
	zapis = str(broj)
	velicina = len(zapis)
	kraj = int(math.ceil(float(len(zapis)) / 2))
	for i in range(kraj):
		if zapis[i] != zapis[velicina-1-i]:
			return False
	print("uspio",broj)
	return True

def main():
	
	dat = open("C-small-attempt0.in",'r')
	dat2 = open("Problem3.out",'w')
	
	T = int(dat.readline())
	
	for i in range(T):
		red = dat.readline().strip()
		red1 = red.split(' ')
		A = int(red1[0])
		B = int(red1[1])
		zbroj = 0
		print(A,B)
		a = int(math.ceil(math.sqrt(A)))
		b = int(math.floor(math.sqrt(B)))+1
		print(a,b)
		for broj in range (a, b):
			if isPalindrom(broj) and isPalindrom(int(math.pow(broj,2))):
				zbroj += 1
		dat2.write("Case #{}: {}\n".format(i+1,zbroj))
	return 0

if __name__ == '__main__':
	main()

