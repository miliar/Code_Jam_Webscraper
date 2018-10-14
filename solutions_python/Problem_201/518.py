"""
x0000000000x
x0000x00000x
x0000x00x00x
x0x00x00x00x
x0xx0x00x00x
x0xx0xx0x00x
x0xx0xx0xx0x
xxxx0xx0xx0x
xxxxxxx0xx0x
xxxxxxxxxx0x
xxxxxxxxxxxx
"""

import fileinput

def insert(spaces, size, number):
	if size not in spaces:
		spaces[size] = 0
	spaces[size] += number

case = 0
count = None
for line in fileinput.input():
	line = line.rstrip()
	if count is None:
		count = int(line)
		continue
	case += 1

	numberOfStalls, people = map(int, line.split())
	spaces = {numberOfStalls: 1}
	while True:
		biggestSpace = max(spaces)
		numberOfBiggestSpaces = spaces[biggestSpace]
		if numberOfBiggestSpaces < people:
			people -= numberOfBiggestSpaces
			if biggestSpace % 2 == 0:
				insert(spaces, biggestSpace / 2,     numberOfBiggestSpaces)
				insert(spaces, biggestSpace / 2 - 1, numberOfBiggestSpaces)
			else:
				insert(spaces, biggestSpace / 2, 2 * numberOfBiggestSpaces)
			del spaces[biggestSpace]
		else:
			print "Case #%s: %s %s" % (case, biggestSpace / 2, (biggestSpace - 1) / 2)
			break
