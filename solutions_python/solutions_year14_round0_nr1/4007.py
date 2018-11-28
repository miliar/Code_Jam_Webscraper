#Much magic, such trick, wow!

# Asumption: input file is always in the anticipated format -> first line of file
# is number of test cases, test case each 10 lines long, line 1 of test case is first choice
# line 6 is second choice, the rest are the rows of card arrangements.

import sys
with open (sys.argv[1], "r") as readfile:
	with open ('Magic-Output.out', "w") as writefile:
		numtest = readfile.readline().rstrip() #number of test cases

		for i in range(1, int(numtest)+1): #for each test case...
			
			choice1 = int(readfile.readline()) #next line must be the first choice

			for j in range(1,5): #for next 4 lines (starts at 1)
				
				if j == choice1: #if it equals the choice, 
					row1 = set(readfile.readline().rstrip().split(' ')) # set row1 to the choice row
				else:
					readfile.readline() #else move on to next line

			choice2 = int(readfile.readline()) #next line must be second choice
			
			for j in range(1,5):
				if j == choice2:
					row2 = set(readfile.readline().rstrip().split(' '))
				else:
					readfile.readline()

			if len(row1&row2) == 1:
				writefile.write('Case #'+ str(i) +': ' + list(row1&row2)[0]+'\n')
			elif len(row1&row2) > 1:
				writefile.write('Case #' + str(i) +": Bad  magician!\n")
			elif len(row1&row2) == 0:
				writefile.write('Case #' + str(i) +": Volunteer cheated!\n")
			else:
				print "something went wrong"
			
