import sys


# Read data file into a list
lines = []
with open(sys.argv[1], "r", encoding="utf-8") as data_file:
	for line in data_file:
		lines.append(line.rstrip('\n'))
		
		
# Get total number of test cases
test_cases = int(lines[0])
del lines[0]


# Process each test case
for i in range(test_cases):
	offset = i * 5
	board = lines[offset] + lines[offset + 1] + lines[offset + 2] + lines[offset + 3]

	totalSpace = board.count('.')
	
	xBoard = board.replace('T', 'X')
	oBoard = board.replace('T', 'O')
	
	# Check for horizontal winner
	found = 0
	for j in range(4):
		sample = xBoard[(j * 4) : ((j + 1) * 4)]
		if (sample.count('X') == 4):
			print('Case #' + str(i + 1) + ": X won")
			found = 1
			break
		sample = oBoard[(j * 4) : ((j + 1) * 4)]
		if (sample.count('O') == 4):
			print('Case #' + str(i + 1) + ": O won")
			found = 1
			break
	if found == 1:
		continue
			
	# Check for vertical winner
	found = 0
	for j in range(4):
		sample = xBoard[j] + xBoard[j + 4] + xBoard[j + 8] + xBoard[j + 12]
		if (sample.count('X') == 4):
			print('Case #' + str(i + 1) + ": X won")
			found = 1
			break
		sample = oBoard[j] + oBoard[j + 4] + oBoard[j + 8] + oBoard[j + 12]
		if (sample.count('O') == 4):
			print('Case #' + str(i + 1) + ": O won")
			found = 1
			break
	if found == 1:
		continue
	
	# Check for diagonal winner
	sample1 = xBoard[0] + xBoard[5] + xBoard[10] + xBoard[15]
	sample2 = xBoard[3] + xBoard[6] + xBoard[9] + xBoard[12]
	if ((sample1.count('X') == 4) or (sample2.count('X') == 4)):
		print('Case #' + str(i + 1) + ": X won")
		continue
	sample1 = oBoard[0] + oBoard[5] + oBoard[10] + oBoard[15]
	sample2 = oBoard[3] + oBoard[6] + oBoard[9] + oBoard[12]
	if ((sample1.count('O') == 4) or (sample2.count('O') == 4)):
		print('Case #' + str(i + 1) + ": O won")
		continue
	
	# Check for tie
	if totalSpace > 0:
		print('Case #' + str(i + 1) + ": Game has not completed")
	else:
		print('Case #' + str(i + 1) + ": Draw")