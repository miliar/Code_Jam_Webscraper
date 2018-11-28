#!/usr/bin/env python

def ispossible(n, m, lawn):

	for ix_row in xrange(n):
		row = lawn[ix_row]
		for ix_col in xrange(m):
			col = map(lambda lawn_row: lawn_row[ix_col], lawn)

			val = lawn[ix_row][ix_col]

			if  len(filter(lambda v: v > val, row)) > 0 and \
				len(filter(lambda v: v > val, col)) > 0:
				return False

	return True

def main():

	test_data = None
	with open('input', 'r') as f:
		test_data = f.read()

	test_data = test_data.split('\n')

	num_test = int(test_data[0])
	test_data_ix = 1
	for test in xrange(num_test):
		# get lawn dimension
		dim_n, dim_m = map(int, test_data[test_data_ix].split(' '))

		# collect lawn desire pattern
		lawn = []
		for i in xrange(dim_n):
			lawn.append(map(int, test_data[test_data_ix + i + 1].split(' ')))

		# main logic
		result = ispossible(dim_n, dim_m, lawn)
		if result:
			print 'Case #%s: YES' % (test + 1)
		else:
			print 'Case #%s: NO' % (test + 1)

		test_data_ix += dim_n + 1


if __name__ == "__main__":
	main()