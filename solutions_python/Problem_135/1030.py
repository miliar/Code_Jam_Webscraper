import sys
input_file = open(sys.argv[1], 'r')
output_file = open(sys.argv[2], 'w')

cases = int(input_file.readline().strip())
for case in range(cases):
	row_r1 = int(input_file.readline().strip())
	grid_r1 = []
	for _ in range(4):
		grid_r1.append(input_file.readline().strip().split())
	row_r2 = int(input_file.readline().strip())
	grid_r2 = []
	for _ in range(4):
		grid_r2.append(input_file.readline().strip().split())
	guess = list(set(grid_r1[row_r1 - 1]) & set(grid_r2[row_r2 - 1]))
	if len(guess) > 1:
		output_file.write('Case #%d: Bad magician!\n' % (case + 1))
	elif len(guess) == 1:
		output_file.write('Case #%d: %s\n' % (case + 1, guess[0]))
	else:
		output_file.write('Case #%d: Volunteer cheated!\n' % (case + 1))
input_file.close()
output_file.close()

