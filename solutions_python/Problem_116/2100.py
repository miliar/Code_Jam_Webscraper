

#######################
##     Google Jam
##    Python template
##
##       by fxxf
##############  reduce(lambda x, y: x + y, ['a','s','d'])


import time
import argparse

if __name__ == '__main__':

	t = time.time()

	parser = argparse.ArgumentParser()
	parser.add_argument("input", help="The input file")
	args = parser.parse_args()

	input = open(args.input, 'r')  # open("./inputs/B-small-practice.in", "r")
	#input = open("./inputs/B-large-practice.in", "r")

	output = open("./output.out", "w")

	## _----------____ INSERT CODE BELOW _____------------_
	CASES = int(input.readline())

	for c in xrange(CASES):

		matrix = []

		for i in xrange(4):
			matrix.append([char for char in input.readline().strip()])
			pass

		input.readline()

		# check -------------------

		x_won = False
		o_won = False
		draw = True

		# horizontal

		o = 0
		x = 0

		for row in xrange(0, 4):
			x = 0
			o = 0
			for r in matrix[row]:
				if r is 'X':
					x += 1
				elif r is 'O':
					o += 1
				elif r is 'T':
					o += 1
					x += 1
				else:
					draw = False

			x_won = x == 4
			o_won = o == 4

			if x_won or o_won:
				break

		#  --------------

		if not x_won and not o_won:
			# vertical

			for v in [[x[i] for x in matrix] for i in [0, 1, 2, 3]]:
				x = 0
				o = 0
				for r in v:
					if r is 'O':
						o += 1
					elif r is 'X':
						x += 1
					elif r is 'T':
						o += 1
						x += 1
					else:
						draw = False

				x_won = x == 4
				o_won = o == 4


				if x_won or o_won:
					break

			if not x_won and not o_won:
			# diagonal

				for v in [[matrix[i][i] for i in [0, 1, 2, 3]], [matrix[i][3-i] for i in [0, 1, 2, 3]]  ] :
					x = 0
					o = 0

					for r in v:
						if r is 'O':
							o += 1
						elif r is 'X':
							x += 1
						elif r is 'T':
							o += 1
							x += 1
						else:
							draw = False

					x_won = x == 4
					o_won = o == 4

					if x_won or o_won:
						break


		toWrite = ""

		if x_won:
			toWrite = "X won\n"
		elif o_won:
			toWrite = "O won\n"
		elif draw:
			toWrite = "Draw\n"
		else:
			toWrite = "Game has not completed\n"

		output.write("Case #%d: %s" % ((c + 1, toWrite)))

		# ------------------------

		pass

	## _----------____ INSERT CODE ABOVE _____------------_

	input.close()
	output.close()

	print 'Time taken %f  seconds' % (time.time()-t)

	pass
