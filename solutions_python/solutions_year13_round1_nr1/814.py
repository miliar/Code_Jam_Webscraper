#############################################
# Google Code Jam 2013						#
# Round 1A									#
# Code written by: Tamara Mendt (Venezuela) #
#############################################

import sys
import string
import time

t0 = time.clock()

try:
	fileInputPointer = open(sys.argv[1], 'r')
	fileOutputPointer = open(sys.argv[2], 'w')
except IOError:
	print("\nInvalid file\n")
	quit()

numberOfCases = int(fileInputPointer.readline().replace('\n',''))
caseNumber = 1
for case in range(0,numberOfCases):
	row = fileInputPointer.readline().replace('\n','').split(' ')
	r = int(row[0])
	ml = int(row[1])
	i = -1
	while(ml>=0):
		i+=2
		resta = (2*i)+(2*r)-1
		ml=ml-resta
	fileOutputPointer.write('Case #'+str(caseNumber)+": "+str(int((i-1)/2))+"\n")
	caseNumber+=1

print("Time: "+str(time.clock()-t0))

