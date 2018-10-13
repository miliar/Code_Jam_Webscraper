import math

infile = open("input.txt", "r")
outfile = open("output.txt", "w")

num_cases = int(infile.readline())
name = "GABRIEL"

for i in range(0, num_cases):
	case = infile.readline()
	temp1, temp2, temp3 = case.split()
	X = int(temp1)
	R = int(temp2)
	C = int(temp3)
	if X == 1:
		name = "GABRIEL"
	elif X > (R * C):
		name = "RICHARD"
	elif (X == 2) and ((R * C) % 2 != 0):
		name = "RICHARD"
	elif (X == 2):
		name = "GABRIEL"
	elif ((R * C) % X != 0) or ((X - 1) > R) or ((X - 1) > C):
		name = "RICHARD"
	else:
		name = "GABRIEL"
	writeline = "Case #" + str(i+1) + ": " + name + "\n"
	outfile.write(writeline)

infile.close()
outfile.close()
