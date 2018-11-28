#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       rope.py
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

def main(args):
	
	#first of all we read the args
	
	if len(args) == 2:
		fp = open(args[1])
		
		ntest = int(fp.readline())
		
		for test in range(ntest):
			# For each test
			
			wires = int(fp.readline())
			
			data = []
			
			n_cross = 0
			
			for wire in range(wires):
				
				# For each wire
				line = fp.readline().split()
				
				a0 = int(line[0])
				b0 = int(line[1])
				
				if data:
					# There is data
					
					for n in range(len(data)):
						row = data[n]
						
						if ( (a0 < row[0]) and (b0 > row[1]) ) or ( (a0 > row[0]) and (b0 < row[1]) ):
							# There is a cross wire
							n_cross += 1
				else:
					# The first wire doesn't cross with any other wire
					data += [[a0, b0]]
			
			# The test is over
			
			print "Case #%d: %d" % (test+1, n_cross)
	
	return 0

if __name__ == '__main__':
	main(sys.argv)
