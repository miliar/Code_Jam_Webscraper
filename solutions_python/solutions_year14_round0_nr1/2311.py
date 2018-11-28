#!/usr/bin/python


'''Google Code Jam 2012
   Dancing Googlers
   Author: Aniket Zamwar
   email: aniketzamwar@gmail.com'''

import sys

if len(sys.argv) != 2:
    print "Please run program: python file.py inputFilename"
    sys.exit()

try:
    f = open(sys.argv[1],'r')
    count = int(f.readline())
except IOError:
    print "Input File could not be opened"
    sys.exit()

case = 1
while count > 0:
	'''
	'''
	count = count - 1
	row_num_1 = int(f.readline())

	matrix1 = [[], [], [], []]
	matrix1[0] = f.readline().strip().split(' ')
	matrix1[1] = f.readline().strip().split(' ')
	matrix1[2] = f.readline().strip().split(' ')
	matrix1[3] = f.readline().strip().split(' ')

	row_num_2 = int(f.readline())

	matrix2 = [[], [], [], []]
	matrix2[0] = f.readline().strip().split(' ')
	matrix2[1] = f.readline().strip().split(' ')
	matrix2[2] = f.readline().strip().split(' ')
	matrix2[3] = f.readline().strip().split(' ')

	#print matrix1
	#print "\n"
	#print matrix2
	flag = 0
	val = -1
	for card1 in matrix1[row_num_1 - 1]:
		for card2 in matrix2[row_num_2 - 1]:
			if card1 == card2:
				flag = flag + 1
				val = card1

	if flag == 0:
		print "Case #" + str(case) + ": Volunteer cheated!"
	elif flag == 1:
		print "Case #" + str(case) + ": " + str(val)
	else: 
		print "Case #" + str(case) + ": Bad magician!"
	case = case + 1




