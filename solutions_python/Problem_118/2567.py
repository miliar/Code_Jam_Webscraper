# -*- coding: utf-8 -*-
import os.path
import math

filename = "C-Fair and Square-small"
inputfilename = os.path.join("input", filename)
outputfilename = os.path.join("output", filename)

def main():
	inputfile = open(inputfilename)
	totalinputcount = int(inputfile.readline())
	outputfile = open(outputfilename, "w+")
	for i in range(totalinputcount):
		currentrange = inputfile.readline().strip()
		rangemin, rangemax = [int(x) for x in currentrange.split(" ")]
		outputfile.write("Case #%s: %s\n" % (i+1, howmanyfairandsquare(rangemin, rangemax+1)))
	inputfile.close()
	outputfile.close()
	pass

def howmanyfairandsquare(rangemin, rangemax):
	counter = 0
	for x in xrange(rangemin, rangemax):
		if isfairandsquare(x):
			counter += 1
	return counter

def isfairandsquare(inputnumber):
	# print "".join(list(str(inputnumber))[::-1])
	if isfair(inputnumber):
		return False
	elif not is_square(inputnumber):
		return False
	elif isfair(int(math.sqrt(inputnumber))):
		return False
	else:
		# print "fair and square ", inputnumber
		return True

def isfair(inputnumber):
	return str(inputnumber) != "".join(list(str(inputnumber))[::-1]);

def is_square(apositiveint):
	if apositiveint == 0:
		return False
	elif apositiveint == 1:
		return True
	x = apositiveint // 2
	seen = set([x])
	while x * x != apositiveint:
		x = (x + (apositiveint // x)) // 2
		if x in seen: return False
		seen.add(x)
	return True

if __name__ == '__main__':
	main()
	pass