#!/usr/bin/python

import sys
import math

def is_palindrome(number):
	word = str(number)
	length = len(word)

	if length == 1:
		return True
	elif word[0] == word[-1]:
		if length == 2:
			return True
		else:
			return is_palindrome(word[1:-1])
	else:
		return False


if __name__ == '__main__':

	filename = sys.argv[1]

	try:
		infile = open(filename)
	except:
		print "Couldn't open file: %s" % filename
		sys.exit(1)

	numcases = int(infile.readline())

	for case in range(1, numcases + 1):

		b, e = infile.readline().strip().split(" ")
		b = int(b)
		e = int(e)

		i = int(math.floor(math.sqrt(b)))
		count = 0

		i_sqr = i**2

		while i_sqr <= e:
			if i_sqr >= b:
				if is_palindrome(i):
					if is_palindrome(i_sqr):
						count += 1

			i += 1
			i_sqr = i**2

		print "Case #%s: %s" % (case, count)


