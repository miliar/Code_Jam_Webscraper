
file = open("A-small-attempt1.in", "r")

num_cases = int(file.readline())

for j in xrange(1, num_cases+1):
    firstchoice = int(file.readline())

    for i in xrange(1,5):
	line = file.readline()
	if (i == firstchoice):
	    firstrow = line.split()
    
    secondchoice = int(file.readline())

    for i in xrange(1,5):
	line = file.readline()
	if(i == secondchoice):
	    secondrow = line.split()

    intersection = [val for val in firstrow if val in secondrow]

    if (len(intersection) == 0):
	print "Case #%d: Volunteer cheated!" %j
    elif (len(intersection) >= 2):
	print "Case #%d: Bad magician!" %j
    else:
	print "Case #%d: %d" %(j, int(intersection[0]))
