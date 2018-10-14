#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       roller.py
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


def main():
	
	# We must check if the user has passed the params
	
	if len(sys.argv) == 2:
		# Correct number of params
		
		# We must read the file
		
		try:
			
			fp = open(sys.argv[1])
			
			# We read the number of cases
			cases = int(fp.readline())
			
			
			for case in range(cases):
				# For each test case we read the test data
				mydata = fp.readline().split()
				
				# We extract the test information
				r = int(mydata[0])
				k = int(mydata[1])
				n = int(mydata[2])
				
				# We extract the groups of people
				mydata = fp.readline().split()
				group_list = [int(i) for i in mydata]
				
				roaller_queue = []
				euros = 0
				# The seats occupied and the flag condition are reset in each loop
				seats_occupied = 0
				condition = True
				
				# For each time
				for time in range(r):
					# For each time we need to fill the roaller coaster until the next group can't fit
					while condition:
						if group_list:
							# The group list is not empty
							if seats_occupied+group_list[0] <= k:
								seats_occupied+=group_list[0]
								roaller_queue.append(group_list.pop(0))
							else:
								condition = False
						else:
							# The group list is empty
							condition = False
					
					# The roaller coaster is full now
					# We earn some money!
					
					euros += seats_occupied
					
					# We put the people in the queue other time
					for people in roaller_queue:
						group_list.append(people)
					
					seats_occupied = 0
					roaller_queue = []
					condition = True
				
				# The roaller coaster can't run more time
				# We print the results
				print "Case #%d: %d" % (case+1, euros)
		except Exception, e:
			print e
			sys.exit(-1)	
	
	return 0

if __name__ == '__main__':
	main()
