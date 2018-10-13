import sys

data = sys.stdin.readlines()
input_data = []
for line in data:
	line = line.rstrip()
	input_data.append(line)

for i in range(1, len(input_data)):
	line = input_data[i]
	line = line.split(' ')
	X = int(line[0])
	R = int(line[1])
	C = int(line[2])

	if (R * C) % X != 0:
		print "Case #" + str(i) + ": RICHARD"
	else:
		if X == 1:
			print "Case #" + str(i) + ": GABRIEL"
		
		elif X == 2:
			print "Case #" + str(i) + ": GABRIEL"

		elif X == 3:
			if R * C == 3:
				print "Case #" + str(i) + ": RICHARD"
			else:
				print "Case #" + str(i) + ": GABRIEL"

		elif X == 4:
			if R * C == 4 or R * C == 8:
				print "Case #" + str(i) + ": RICHARD"
			else:
				print "Case #" + str(i) + ": GABRIEL"




