# house of N by M meters

# h, height of maximum grass height = 1 -> 100 milimeters
# height can only be set when outside of grass
# mower goes in straight line

# 1m wide mower
# mower can enter on any part of the edge of the lawn

# Want to know if patterns all possible


# initially, ALL GRASS IS 100 mm high

INPUT_SAMPLE = 'B-sample.in.txt'
INPUT_SMALL  = 'B-small-attempt1.in.txt'
INPUT_LARGE  = 'B-large.in.txt'

INPUT = INPUT_LARGE

OUTPUT_POSSIBLE   = "YES"
OUTPUT_IMPOSSIBLE = "NO"


f = open("output.txt", 'w')

lines = open(INPUT, 'r').readlines()
lines = [x.rstrip('\n') for x in lines]

# 1st line = no of test cases
noTestCases = int(lines[0])
lines = lines[1:]

for currTestCase in xrange(0, noTestCases):
	print currTestCase

	if (currTestCase !=0):
		f.write("\n")
	f.write('Case #' + str(currTestCase+1) + ": ")

	#  2nd line: N M
	N = int(lines[0].split(' ')[0])
	M = int(lines[0].split(' ')[1])
	lines = lines[1:]

	# Next follow N rows with M values
	# a[i,j] describes the desired height

	# construct the lawn
	lawn = []
	for currRow in xrange(0, N):
		lawn.append([int(x) for x in lines[currRow].split(' ')])

	# Basically, a point on the lawn can be 'achieved' (the height of the grass)
	# if the value on either its row or column, it represents the maximum

	# an array of bools, that says if a point can be achieved
	# keep the result from analysing the rows and columns separate
	# more memory, but clean and speed doesn't matter here
	lawn_result = []

	for row_no in xrange(0,N):
		tmp = []
		for col_no in xrange(0,M):
			tmp.append(False)
		lawn_result.append(tmp)

	# 1st, do the rows
	# find the maximum of each row

	for row_no in xrange(0,N):
		lawn_row = lawn[row_no]
		maximum = max(lawn_row)

		lawn_result[row_no] = [ x>=maximum for x in lawn_row]

	answer = None


	# 2nd, do the columns
	# if a point is not the maximum in its column and it also wasn't in its row
	# then it's impossible to achieve the pattern
	for col_no in xrange(0,M):
		lawn_col = []

		for row_no in xrange(0,N):
			lawn_col.append(lawn[row_no][col_no])

		maximum = max(lawn_col)

		for row_no in xrange(0,N):

			biggest_in_col = (lawn_col[row_no] >= maximum)

			if biggest_in_col == True :
				lawn_result[row_no][col_no] = True
			elif lawn_result[row_no][col_no] == False:
				answer = OUTPUT_IMPOSSIBLE
				break

		if answer is not None:
			break

	if answer is None:
		answer = OUTPUT_POSSIBLE

	f.write(answer)

	# trim the remaining lines for the next test case
	lines = lines[N:]

