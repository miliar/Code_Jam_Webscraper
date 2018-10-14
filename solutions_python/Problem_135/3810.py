n = int(raw_input())

# read in n lines of input and store them in a dictionary
for i in range(n):

	first_row = []
	second_row = []

	#get first row:
	row_number = int(raw_input())
	for j in range(4):
		row = raw_input().split()
		if j + 1 == row_number:
			first_row = row

	#get second row:
	row_number = int(raw_input())
	for j in range(4):
		row = raw_input().split()
		if j + 1 == row_number:
			second_row = row

	matches = []

	for x in second_row:
		if x in first_row:
			matches.append(x)

	if len(matches) == 1:
		print "Case #%s: "%(i+1) +  matches[0]
	elif len(matches) == 0:
		print "Case #%s: "%(i+1) +   "Volunteer cheated!"
	else: 
		print "Case #%s: "%(i+1) +  "Bad magician!"



