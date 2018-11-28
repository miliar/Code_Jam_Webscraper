import math
message = open("D-small-attempt1.in", 'r')
#message = open("dtest.in", 'r')
lines = message.readlines()
cases = 0
case = 0
for line in lines:
	if case == 0:
		cases = line
		case = 1
		continue
	inputs = line.split()
	X = int(inputs[0])
	R = int(inputs[1])
	C = int(inputs[2])
	if (R*C) % X != 0 or math.ceil(X / 2) > R or math.ceil(X / 2) > C or X >= 7 or (X >= 4 and (R == 2 or C == 2)) or (X == 6 and R*C < 24 and (R == 3 or C == 3)):
		print("Case #" + str(case) + ": RICHARD")
		case = case + 1
		continue
	else:
		print("Case #" + str(case) + ": GABRIEL")
		case = case + 1
		continue
