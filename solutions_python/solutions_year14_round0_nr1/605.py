# Open files
inf = open('A-small-attempt0.in', 'r')
outf = open('out.txt', 'w')

# Read in number of test cases
n = int(inf.readline().strip())

#Loop through test cases
for i in xrange(n):
	ans = ''
	board1 = []
	board2 = []
	c1 = int(inf.readline().strip())
	for j in xrange(4):
		board1.append(inf.readline().strip().split())
	c2 = int(inf.readline().strip())
	for j in xrange(4):
		board2.append(inf.readline().strip().split())

	possible = list(set(board1[c1-1]).intersection(set(board2[c2-1])))

	if not possible :
		ans = 'Volunteer cheated!'
	elif len(possible) > 1:
		ans = 'Bad magician!'
	else:
		ans = str(possible[0])

	outf.write('Case #%d: %s\n' % (i+1, ans))

# Close input and output files
inf.close()
outf.close()