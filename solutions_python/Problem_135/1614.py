# -*-coding:Utf-8 -*

import sys

# Parse args
with open("A-small-attempt1.in") as f:
	arg = f.readlines()

T = arg[0]
column = [[0 for y in range(2)] for x in range(int(T))]
matrix = [[0 for y in range(2)] for x in range(int(T))]
for ct in range(0, int(T)):
	column[ct][0] = arg[1+ct*10]
	matrix[ct][0] = [0 for x in range(4)]
	matrix[ct][0][0] = arg[2+ct*10]
	matrix[ct][0][1] = arg[3+ct*10]
	matrix[ct][0][2] = arg[4+ct*10]
	matrix[ct][0][3] = arg[5+ct*10]
	column[ct][1] = arg[6+ct*10]
	matrix[ct][1] = [0 for x in range(4)]
	matrix[ct][1][0] = arg[7+ct*10]
	matrix[ct][1][1] = arg[8+ct*10]
	matrix[ct][1][2] = arg[9+ct*10]
	matrix[ct][1][3] = arg[10+ct*10]

f = open('A-small.out','w')

# Compute each case
for ct in range(int(T)):
	# Print data in memory
	#print "case number " + str(ct)
	#print "  column chosen first: " + column[ct][0]
	#print "  column chosen second: " + column[ct][1]
	#print "  first matrix: "
	#print "    " + matrix[ct][0][0]
	#print "    " + matrix[ct][0][1]
	#print "    " + matrix[ct][0][2]
	#print "    " + matrix[ct][0][3]
	#print "  second matrix: "
	#print "    " + matrix[ct][1][0]
	#print "    " + matrix[ct][1][1]
	#print "    " + matrix[ct][1][2]
	#print "    " + matrix[ct][1][3]
	
	# Get possible numbers
	numbers = [0 for x in range(2)]
	numbers[0] = matrix[ct][0][int(column[ct][0])-1].split()
	numbers[1] = matrix[ct][1][int(column[ct][1])-1].split()

	# Check for intersection
	case = "Volunteer cheated!"
	for x in range(4):
		for y in range(4):
			if numbers[0][x] == numbers[1][y]:
				if case == "Volunteer cheated!" :
					case = str(numbers[0][x])
				else:
					case = "Bad magician!"
	
	# Print output
	f.write ("Case #" + str(ct+1) + ": " + case + "\n")
	
