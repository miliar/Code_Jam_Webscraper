import sys
input = open(sys.argv[1], 'r')

for x in xrange(int(input.readline().strip())):
	firstRow = int(input.readline().strip())

	for i in xrange(4):
		if (i + 1) == firstRow:
			row1 = map(int,input.readline().split())
		else:
			input.readline()

	secondRow = int(input.readline().strip())

	for j in xrange(4):
		if (j + 1) == secondRow:
			row2 = map(int,input.readline().split())
		else:
			input.readline()

	current = -1
	badMagician = False

	for num in row1:
		if row2.count(num) > 0:
			if current != -1:
				badMagician = True
				break
			else:
				current = num

	if current == -1:
		print('Case #%d: Volunteer cheated!' % (x+1))
	elif badMagician:
		print('Case #%d: Bad magician!' % (x+1))
	else:
		print('Case #%d: %d' % (x+1,current))

input.close()