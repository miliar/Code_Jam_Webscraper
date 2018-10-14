def solve_problem(input_file):

	# Open the input file
	fp = open(input_file)
	lines = fp.readlines()
	lines = [ s.rstrip("\n") for s in lines ]
	fp.close()

	# Get the number of cases
	cases = int( lines[0] )

	# Loop through them
	fp = 1
	for i in xrange(cases):

		# p = max letters on key
		# k = number of keys available
		# l = number of letters in alphabet
		p, k, l = [ int(x) for x in lines[fp].split( " " ) ]
		fp += 1

		# the next line is the frequency of each letter
		freqs = [ int(x) for x in lines[fp].split( " " ) ]
		fp += 1

		# check we have a full list
		if len(freqs) != l: raise SyntaxError, "wrong number of letter frequencies"

		# make a list of empty lists for the new keylayout
		layout = [ [] for x in range(k) ]

		# decorate the letters and sort
		letters = zip( freqs, range(l) )
		letters.sort()
		letters.reverse()
		sorted = zip( *letters )

		# now assign letters to keys sequentially
		j = 0
		for letter in sorted[1]:
			layout[j % k].append(letter)
			j += 1
		
		# check if we have the impossible case
		max = 0
		for key in layout:
			if len(key) > max: max = len(key)
		if max > p:
			print "Case #%i: Impossible" % i+1
			continue

		# now we need to calculate the required keypresses
		presses = 0
		for letter in letters:

			# find how deep it is
			depth = None
			for key in layout:
				try:
					depth = key.index(letter[1]) + 1
				except ValueError:
					continue

			# if depth is none we have a problem
			if depth is None: raise StandardError, "the user will never see this"

			# add the keypresses
			presses += depth * letter[0]

		# output the statement
		print "Case #%i: %i" % (i+1, presses)

solve_problem("1.in")
	
