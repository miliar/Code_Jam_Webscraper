#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       sin título.py
#       
#       Copyright 2010 Eusebio <eusebio.aguilera@gmail.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import sys

import psyco
psyco.full()

def my2sum(n):
	result = 0
	for i in range(n):
		result += 2**i
	
	return result


def main():
	
	if len(sys.argv) == 2:
		# Correct number of params
		
		# We must read the file
		
		try:
			
			fp = open(sys.argv[1])
			
			# We read the number of cases
			cases = int(fp.readline())
			
			
			for case in range(cases):
				
				result = 'OFF'
				
				mydata = fp.readline().split()
				
				n = int(mydata[0])
				k = int(mydata[1])
				
				temp = 2 ** n - 1
				
				if k == temp:
					result = 'ON'
				elif k > temp:
					k -= temp
					
					if k % (2 ** n) == 0:
						result = 'ON'
			
				# We print the results
				print "Case #%d: %s" % (case+1, result)
		except Exception, e:
			print e
			sys.exit(-1)	
	
	return 0

if __name__ == '__main__':
	main()
