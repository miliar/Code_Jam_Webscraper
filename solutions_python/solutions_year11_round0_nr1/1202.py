#! /usr/bin/env python


import sys
import os
import string



infile = open(sys.argv[1], "r")
outfile = open("outa", "w")

T = int(infile.readline())
#print T
for i in range(1, T+1):
	B = []	# blues instructions
	Bindex = 1
	O = []	# oranges instructions
	Oindex = 1
	intrs = [] # all instructions
	line = infile.readline().strip().split()
	#print line
	Nintrs = int(line.pop(0))
	#print line
	#print Nintrs, range(Nintrs)
	for j in range(Nintrs):
		#print j
		#print line
		who = line.pop(0)
		where = int(line.pop(0))
		comb = who, where
		#print comb
		intrs.append(comb)
		if who == 'O':
			O.append(where)
		else:
			B.append(where)
	# print intrs
	# print B
	# print O
	# print
	count=0
	currB=1;
	currO=1
	for j in range(Nintrs):
		current = intrs.pop(0)
		#print current,
		#print("currB = %d, Bind = %d, currO = %d, Oind = %d,  count = %d\n" % (currB, Bindex, currO, Oindex, count))
		if len(B) == 0:	# no more B instructions, remain at location
			currB = Bindex
		else:
			currB = B[0]
		if len(O) == 0:	# no more O instructions, remain at location
			currO = Oindex
		else:
			currO = O[0]
		#print current, B, O
		#print("currB = %d, Bind = %d, currO = %d, Oind = %d,  count = %d" % (currB, Bindex, currO, Oindex, count))
		if (current[0] == 'O'):	# current instruction is for O
			
			while (Oindex != currO):	# move while current ind of orange is not at the spot
				if (Oindex < currO):
					Oindex += 1
				elif (Oindex > currO):
					Oindex -= 1
				if (Bindex < currB):
					Bindex += 1
				elif (Bindex > currB):
					Bindex -=1
				count += 1
			if (Oindex == currO):
				if (Bindex < currB):
					Bindex += 1
				elif (Bindex > currB):
					Bindex -=1
				count += 1	#push button
			O.pop(0)
		elif (current[0] == 'B'):
			
			while (Bindex != currB):	# move while current ind of orange is not at the spot
				if (Oindex < currO):
					Oindex += 1
				elif (Oindex > currO):
					Oindex -= 1
				if (Bindex < currB):
					Bindex += 1
				elif (Bindex > currB):
					Bindex -=1
				count += 1
			if (Bindex == currB): 
				if (Oindex < currO):
					Oindex += 1
				elif (Oindex > currO):
					Oindex -= 1
				count+=1
			B.pop(0)
		#print current, B, O
		#print("currB = %d, Bind = %d, currO = %d, Oind = %d,  count = %d\n" % (currB, Bindex, currO, Oindex, count))
	outfile.write("Case #%d: %d\n" % (i, count))
	
infile.close()
outfile.close()