filename = 'A-large.in'
output	=	'output.txt'

openfile = open(filename, 'r')
outputfile = open(output, 'w')

openfile.readline()
K = 0

def flip(line, a, b):
	for point in range(a, b+1):
		if line[point] == '+':
			line = line[:point] + '-' + line[point +1:]
		else:
			line = line[:point] + '+' + line[point +1:]
	return line

def sequence(line):
	flips = 0
	if '-' not in line:
		return 0
	if K > len(line) or K == 0:
		return 'IMPOSSIBLE'
	for a in range(0, len(line) - K + 1):
		if line[a] == '-':
			line = flip(line, a, a + K -1)
			flips = flips + 1
	if '-' in line:
		return "IMPOSSIBLE"
	return flips

case = 1
for line in openfile:
	K = int(line[line.index(' '):])
	print line
	while line[-1] != '-' and line[-1] != '+':
		line = line[:len(line)-1]
	flips = sequence(line)
	print flips
	print '\n'
	outputfile.write('Case #' + str(case) + ': ' + str(flips) + '\n')
	case = case + 1