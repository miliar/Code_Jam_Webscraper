import sys
import re
#import math

f = open(sys.argv[1])

cases = int(f.readline())
#print cases

for x in range(0, cases):

	lines_count = int(f.readline())

	lines = []
	normalized = []
	for l in range(0, lines_count):
		line = f.readline().strip()
		lines.append(line)
		# normalize!
		nline = re.sub(r'(.)\1+', r'\1', line)
		normalized.append(nline)
	#print lines
	#print normalized

	# check if solvable
	solvable = True
	for nline in normalized:
		if nline != normalized[0]:
			solvable = False
			break
	if not solvable:
		print 'Case #%d: Fegla Won' % (x+1)
		continue
	# check if all are equal
	all_equal = True
	for line in lines:
		if line != lines[0]:
			all_equal = False
	if all_equal:
		print 'Case #%d: 0' % (x+1)
		continue

	# count repeats in each line
	line_repeats = []
	for line in lines:
		repeats = []

		rep = 1
		last_char = ''
		for new_char in line:
			if new_char != last_char:
				if last_char != '':
					repeats.append(rep)
				rep = 1
			else:
				rep = rep + 1
			last_char = new_char
		repeats.append(rep)
		line_repeats.append(repeats)

	#print line_repeats

	# now, time for solving!!
	letters = normalized[0]
	minimal_moves = 0
	for lt in range(0, len(letters)):
		letter = letters[lt]

		#print letter,
		amount_min = 9999
		amount_max = 0
		for lrep in line_repeats:
			letter_repeats = lrep[lt]
			#print letter_repeats,
			if letter_repeats > amount_max:
				amount_max = letter_repeats
			if letter_repeats < amount_min:
				amount_min = letter_repeats
		#print
		# now we have min and max
		lettr_moves = 0
		for moves_candidate in range(amount_min, amount_max+1):
			for lrep in line_repeats:
				letter_repeats = lrep[lt]
				difference = abs(letter_repeats - moves_candidate)
				if difference > lettr_moves:
					lettr_moves = difference
		#print letter, lettr_moves
		minimal_moves = minimal_moves + lettr_moves
	print 'Case #%d: %d' % (x+1, minimal_moves)

f.close()

