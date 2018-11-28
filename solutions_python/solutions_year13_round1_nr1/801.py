
#######################
##     Google Jam
##    Python template
##
##       by fxxf
##############

# import time
import argparse

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

		r, t = map(int, input.readline().split())

		circles = -1

		while t >= 0 :

			area = (r+1)**2 - (r ** 2)

			t -= area

			r += 2

			circles +=1 

			pass

		output.write("Case #%d: %d\n" % ((c+1, circles)))

		pass

	## _----------____ INSERT CODE ABOVE _____------------_

	input.close()
	output.close()

	# print 'Time taken %f  seconds' % (time.time()-t)

	pass
