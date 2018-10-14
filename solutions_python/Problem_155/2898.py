infile = open('A-large.in', 'r')
outfile = open('A-large.out', 'w')

T = int(infile.readline())
case = 1

while (case <= T):
	# do work
	sMax, sList = infile.readline().split(' ')
	standing = 0
	friends = 0

	for shyness in xrange(0,int(sMax)+1):
		if (standing < shyness):
			friends += shyness - standing
			standing += shyness - standing
		standing += int(sList[shyness])
	# write result
	outfile.write('Case #' + str(case) + ': ' + str(friends) +'\n')
	case+= 1

infile.close()
outfile.close()