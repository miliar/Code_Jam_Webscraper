import fileinput
import re

# takes a string
def isTidy(n):
	last = 0
	for digit in n:
		if digit < last:
			return False
		last = digit
	return True

count = None
case = 0

parts = re.compile('^(.*?)(0*)$')
for line in fileinput.input():
	line = line.rstrip()
	if count is None:
		count = int(line)
		continue
	case += 1

	if isTidy(line):
		print "Case #%s: %s" % (case, line)
		continue

	# Loop until zeroes at the end, the rest is tidy and n-2 < n-1:
	while True:
		m = parts.match(line)
		leftPart = m.group(1)
		rightPart = m.group(2)
		secondLastDigit = 0 if len(leftPart) == 1 else leftPart[-2]
		if isTidy(leftPart) and secondLastDigit < leftPart[-1]:
			break

		# Set the last non-zero number to zero
		line = "%s0%s" % (leftPart[:-1], rightPart)
		continue

	# Convert to int, subtract one
	print "Case #%s: %s" % (case, int(line) - 1)
