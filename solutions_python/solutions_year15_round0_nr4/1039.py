import fileinput

line_num = 0
answers = []
f = open('answers.txt', 'w')

for line in fileinput.input():

	# Don't need number of test cases for this solution; ignore first line.
	if line_num == 0:
		pass
	else:
		f.write('Case #%s: ' % line_num)

		data = line.split(' ')
		x = int(data[0])
		r = int(data[1])
		c = int(data[2])

		area = r * c
		if area >= (x * (x-1)) and area % x == 0:
			f.write('GABRIEL')
			print 'GABRIEL'
		else:
			f.write('RICHARD')
			print 'RICHARD'

		f.write('\n')

	line_num += 1

f.close()