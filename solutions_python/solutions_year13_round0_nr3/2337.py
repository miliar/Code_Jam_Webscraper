
#######################
##     Google Jam
##    Python template
##
##       by fxxf
##############

# import time
import argparse
from math import sqrt

if __name__ == '__main__':

	# t = time.time()

	parser = argparse.ArgumentParser()
	parser.add_argument("input", help="The input file")
	args = parser.parse_args()

	input = open(args.input, 'r')

	output = open("./output.out", "w")

	## _----------____ INSERT CODE BELOW _____------------_
	CASES = int(input.readline())

	for c in xrange(CASES):

		l, u = map(int, input.readline().split())

		found = 0
		for i in xrange(l, u + 1):
			if str(i) == str(i)[::-1]:

				sq = sqrt(i)

				if sq.is_integer():
					sq = int(sq)
					if str(sq) == str(sq)[::-1]:
						found += 1
			pass

		output.write("Case #%d: %d\n" % ((c + 1, found)))

		pass

	## _----------____ INSERT CODE ABOVE _____------------_

	input.close()
	output.close()

	# print 'Time taken %f  seconds' % (time.time()-t)

	pass
