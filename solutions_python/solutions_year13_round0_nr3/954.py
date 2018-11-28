import sys
import math

data = open(sys.argv[1]).read().split("\n")

cases = int(data.pop(0))
for case in range(cases):
	print "Case #%d:" % (case + 1),
	start, end = map(int, data.pop(0).split())
	# get the roots
	rstart = int(math.ceil(math.sqrt(start)))
	rend = int(math.sqrt(end))
	fasqs = 0
	for i in range(rstart, rend + 1):
		# Check if number is palindrome
		if str(i) == str(i)[::-1]:
			# Check if square is palindrome
			strsq = str(i**2)
			if strsq == strsq[::-1]:
				fasqs += 1
	print fasqs