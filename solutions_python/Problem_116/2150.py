

def main():
	input_file = open ('tic.in', 'r')
	tests = int(input_file.readline())
	for t in xrange(tests):
		lines = [0] * 5
		columns = [0] * 5
		principal = 0;
		secondary = 0;
		done = 0
		draw = True
		for i in xrange(4):
			values = input_file.readline();
			for j in xrange(len(values)):
				if done == 1:
					continue
				if values[j] == "X":
					columns[j] = columns[j] + 1;
					lines[i] = lines[i] + 1;
					if i == j:
						principal = principal + 1
					if i + j == 3:
						secondary = secondary + 1
				elif values[j] == "O":
					columns[j] = columns[j] - 1;
					lines[i] = lines[i] - 1;
					if i == j:
						principal = principal - 1
					if i + j == 3:
						secondary = secondary - 1
				elif values[j] == "T":
					columns[j] = columns[j] + 10;
					lines[i] = lines[i] + 10;
					if i == j:
						principal = principal + 10
					if i + j == 3:
						secondary = secondary + 10
				elif values[j] == ".":
					draw = False

				if (columns[j] == 4 or columns[j] == 13 or
					principal == 4 or principal == 13 or
					secondary == 4 or secondary == 13 or
					lines[i] == 4 or lines[i] == 13):
					print "Case #" + str(t+1) + ": X won"
					done = 1
				if (columns[j] == -4 or columns[j] == 7 or
					principal == -4 or principal == 7 or
					secondary == -4 or secondary == 7 or
					lines[i] == -4 or lines[i] == 7):
					print "Case #" + str(t+1) + ": O won"
					done = 1


		if done == 0:
			if draw == False:
				print "Case #" + str(t+1) + ": Game has not completed"
			else:
				print "Case #" + str(t+1) + ": Draw"
		input_file.readline();




if __name__ == "__main__":
	main()
