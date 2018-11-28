# Helper Functions

def case_result(row1, row2):
	"""Returns the output of the case based on the number of elements that row1
	and row2 have in common.
	Assumes that the numbers in each of row1 and row2 are distinct."""
	intersection = set(row1) & set(row2)
	if len(intersection) == 0:
		return "Volunteer cheated!"
	elif len(intersection) == 1:
		return list(intersection)[0]
	else:
		return "Bad magician!"

### MAIN PROGRAM ###

input_filename  = "A-small-attempt0.in"
output_filename = "A-sample-ans0.txt"

BOARD_LENGTH = 4   # Number of rows

f  = open(input_filename, "r")
g = open(output_filename, "w")

number_of_cases = int(f.readline())

case_cnt = 0
while case_cnt < number_of_cases:
# parse the 2 boards. just read in the row that the volunteer said
	row_number = int(f.readline())
	for i in range(1, BOARD_LENGTH + 1):
		if i == row_number:
			row1 = f.readline().strip().split(' ')
		else:
			f.readline()
	row_number = int(f.readline())
	for i in range(1, BOARD_LENGTH + 1):
		if i == row_number:
			row2 = f.readline().strip().split(' ')
		else:
			f.readline()

	# main logic of problem
	result = case_result(row1, row2)

	# output to screen & file
	print   "Case #" + str(case_cnt+1) + ": " + result
	g.write("Case #" + str(case_cnt+1) + ": " + result + "\n")
	
	# move on to the next case
	case_cnt += 1

f.close()
g.close()

