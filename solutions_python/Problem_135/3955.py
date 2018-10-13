"""
Input is:

3             // how many test cases
2             // which row the card is in
1 2 3 4       //
5 6 7 8        |
9 10 11 12     | Array of  cards (4x4)
13 14 15 16    |
3             // repeats without how many test cases
1 2 5 4
3 11 6 15
9 10 7 12
13 14 8 16

"""
filename = "A-small-attempt0.in"

with open(filename, "r") as inputfile:
	inputfiledata = inputfile.read().split('\n')
	numberoftestcases = int(inputfiledata[0])
	
	testcases = []
	loopsforinput = 0
	while loopsforinput < numberoftestcases * 2:
		
		# sets where to read from the file
		n = loopsforinput * 5
		
		# get the correct line for the test-case
		linetoget = int(inputfiledata[1+n])

		# get the line and turn it into an array of ints
		linegotten = inputfiledata[linetoget+n+1]
		linegotten = map(int, linegotten.split(" "))
		
		# create the current-case array and append to global array
		currentcase = [linetoget, linegotten]
		testcases.append(currentcase)

		# +1 to the loop counter
		loopsforinput += 1

for number in range(1, numberoftestcases + 1):
	
	# set where the loop does compare
	n = (number) * 2

	intersection = list(set(testcases[n-2][1]).intersection(testcases[n-1][1]))

	# if only one intersection is found, good!
	# if more than one intersection, magician screwed up
	# if no intersection, volunteer is lying
	if len(intersection) == 1:
		print "Case #%d: %d" % (number, intersection[0])
	elif len(intersection) > 1:
		print "Case #%d: Bad magician!" % (number)
	elif len(intersection) == 0:
		print "Case #%d: Volunteer cheated!" % (number)