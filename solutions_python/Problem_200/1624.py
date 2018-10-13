filename = 'B-large.in'
output	=	'output.txt'

openfile = open(filename, 'r')
outputfile = open(output, 'w')

openfile.readline()

case = 1
for line in openfile:
	temp = []
	for a in range(0,len(line)):
		if line[a].isdigit():
			temp.append(int(line[a]))
	a = 1
	while a < len(temp):
		print a
		print len(temp)
		print '\n'
		if temp[a] < temp[a - 1]:
			for b in range(a, len(temp)):
				temp[b] = 9
			temp[a - 1] = temp[a - 1] - 1
			a = a - 1
			if a == 0:
				a = 1
		else:
			a = a + 1
		
		
	value = ''
	for a in temp:
		value = value + str(a)
	outputfile.write('Case #' + str(case) + ': ' + str(int(value)) + '\n')
	case = case + 1
			