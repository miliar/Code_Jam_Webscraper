input = open('input.txt', 'r')
outputf = open('output.txt', 'w')

T = int(input.readline())

for tc in range(1, T+1):
	row = int(input.readline())
	for x in range(0, 4):
		if row - x == 1:
			row1numbers = input.readline()
		else:
			input.readline()
	
	row = int(input.readline())
	for x in range(0, 4):
		if row - x == 1:
			row2numbers = input.readline()
		else:
			input.readline()

	row1 = row1numbers.rstrip().split(" ")
	row2 = row2numbers.rstrip().split(" ")
	
	inter = list(set(row1) & set(row2))
	
	if len(inter) == 0:
		output = "Case #" + str(tc) + ": Volunteer cheated!"
	elif len(inter) == 1:
		output = "Case #" + str(tc) + ": "+str(inter[0])
	else:
		output = "Case #" + str(tc) + ": Bad magician!"

	outputf.write(output + "\n")