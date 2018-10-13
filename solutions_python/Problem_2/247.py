import sys

# Convert a time to minutes
# eg "09:00" to "9*60"
def to_mins(input_string):

	# Get the two parts
	hours, mins = input_string.split(":")
	hours = int(hours) ; mins = int(mins)

	# Calculate and return
	return hours*60+mins

# Process times
# eg "09:00 12:00" to "(9*60,12*60)"
def process_time(input_string):

	# Get the two parts
	a, b = input_string.split(" ")

	# Convert from times to integer minutes
	a = to_mins(a)
	b = to_mins(b)

	# Return tuple
	return (a,b)

# Main routine
def run_test(input_file):

	# Open the file
	fp = open(input_file, "r")
	if fp is None: raise IOError, "Cannot open input file"
	lines = fp.readlines()
	lines = [ s.rstrip("\n") for s in lines ]
	fp.close()

	# Get the number of cases
	cases = int( lines[0] )

	# Loop through them
	fptr = 1
	for i in range(cases):

		# Get the turnaround time
		turnaround = int( lines[fptr] )
		fptr += 1

		# Get the number of a and b times
		na, nb = lines[fptr].split(" ")
		na = int(na) ; nb = int(nb)
		fptr += 1

		# Get the a to b trains
		a2b = lines[fptr:fptr+na]
		fptr += na

		# Get the b to a trains
		b2a = lines[fptr:fptr+nb]
		fptr += nb

		# Map both from two strings to tuples of integers
		a2b = [ process_time(x) for x in a2b ]
		b2a = [ process_time(x) for x in b2a ]

		# Get the list of train times
		if a2b:
			a_depart, b_arrive = zip(*a2b)
		else:
			a_depart = []; b_arriva = []
		if b2a:
			b_depart, a_arrive = zip(*b2a)
		else:
			b_depart = []; a_arrive = []

		# Add the turnaround time to the arrival times
		a_arrive = [ x + turnaround for x in a_arrive ]
		b_arrive = [ x + turnaround for x in b_arrive ]

		# Attach a +- and merge (- means arrive, + means depart so sorting works out)
		a = [ (x, -1) for x in a_arrive ] + [ (x, 1) for x in a_depart ]
		b = [ (x, -1) for x in b_arrive ] + [ (x, 1) for x in b_depart ]

		# Sort the lists
		a.sort()
		b.sort()

		# Undecorate the lists
		a = zip(*a)[1]
		b = zip(*b)[1]

		# Calculate a running total down each list and find the maximum value
		# this is the number of trains that should be there initially
		p = 0 ; q = 0
		s = 0
		for x in a:
			s += x
			if s > p: p = s
		s = 0
		for x in b:
			s += x
			if s > q: q = s

		# Output the answer line
		print "Case #%i: %i %i" % (i+1,p,q)		

run_test(sys.argv[1])

