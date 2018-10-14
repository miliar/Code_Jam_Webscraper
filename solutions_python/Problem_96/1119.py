# Solution to B. Dancing With the Googlers

filename = "B-large.in"
infile = open(filename, 'r')

outfile = open("output.txt", 'w')

first_line = True
case = 1

for line in infile:
	if first_line:
		first_line = False
		continue
	ints = []
	for i in line.split(" "):
		ints.append(int(i))
	num_googlers = ints[0]
	surprising_scores = ints[1]
	lbound = ints[2]
	totals = []
	
	for i in range(3, num_googlers + 3):
		totals.append(ints[i])
	greater_scores = 0
	
	for i in totals:
		if i >= lbound:
			if i - lbound - 2*(lbound - 1) >= 0:	# Must've gotten a high score of greater than or equal to lbound
				greater_scores += 1
			elif surprising_scores > 0 and i >= lbound + 2*(lbound - 2):	# Could've gotten a high score of greather than or equal to lbound, but only if it was surprising.
				greater_scores += 1
				surprising_scores -= 1
	outfile.write("Case #%i: %i\n" % (case, greater_scores))
	case += 1
	
infile.close()
outfile.close()