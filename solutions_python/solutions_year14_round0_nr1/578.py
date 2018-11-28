
f = open('/Users/Wanli/Downloads/A-small-attempt0.in.txt')
# f = open('input.txt')
ncases = int(f.readline())

for case in range(ncases):
	num1 = int(f.readline())
	square1 = []
	square1.append([int(x) for x in f.readline().split()])
	square1.append([int(x) for x in f.readline().split()])
	square1.append([int(x) for x in f.readline().split()])
	square1.append([int(x) for x in f.readline().split()])

	num2 = int(f.readline())
	square2 = []
	square2.append([int(x) for x in f.readline().split()])
	square2.append([int(x) for x in f.readline().split()])
	square2.append([int(x) for x in f.readline().split()])
	square2.append([int(x) for x in f.readline().split()])	

	matches = []
	row1 = square1[num1-1]
	row2 = square2[num2-1]

	for num in row1:
		if num in row2:
			matches.append(num)

	if len(matches) == 1:
		print 'Case #%d: %d' % (case+1, matches[0])
	elif len(matches) == 0:
		print 'Case #%d: %s' % (case+1, 'Volunteer cheated!')
	else:
		print 'Case #%d: %s' % (case+1, 'Bad magician!')
