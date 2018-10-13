#!python2.7
import fileinput, sys

ROWS = 4
OFFSET_COUNT = ROWS + 1
TURNS = 2

input_text = []

for line in fileinput.input():
	input_text.append(line.strip())

T = int(input_text[0])

for t in xrange(T):
	cards_in_both = set(xrange(1, 16 + 1))
	offset = (t * OFFSET_COUNT * TURNS) + 1
	for turn in xrange(2):
		offset += (turn * OFFSET_COUNT)
		row = int(input_text[offset])
		if row < 1 or row > 4:
			print "Bad guess number."
			sys.exit(1)
		cards_in_both &= set(map(int, input_text[row + offset].split()))

	print "Case #" + str(t + 1) + ":",
	if len(cards_in_both) > 1:
		print "Bad magician!"
	elif len(cards_in_both) == 0:
		print "Volunteer cheated!"
	else:
		print cards_in_both.pop()

