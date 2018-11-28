from __future__ import print_function
import sys

def solve_tc(n):
	# Smaller than 10, it is correct
	if len(n) == 1:
		return n

	# Return if it is already a tidy number
	ints = [int(x) for x in n]
	is_tidy = all(ints[i] <= ints[i+1] for i in xrange(len(ints)-1))
	if is_tidy:
		return n
	
	while not is_tidy:
		is_tidy = True

		for i in xrange(len(ints)-1, 0, -1):
			if ints[i] < ints[i-1]:
				ints[i-1] -= 1
				for j in xrange(i, len(ints)):
					ints[j] = 9
				is_tidy = False
				break

	if ints[0] == 0:
		return ''.join([str(x) for x in ints[1:]])	
	return ''.join([str(x) for x in ints])

if __name__ == '__main__':
	# read data
	filename = sys.argv[1]

	with open(filename, 'r') as in_file, open(filename.replace('in', 'out'), 'w') as out_file:
		tc_count = int(in_file.readline())
		for i in range(tc_count):
			n = in_file.readline()
			if n[-1] == '\n':
				n = n[:-1]
			sol = solve_tc(n)

			print('Case #%d: %s' %(i+1, sol), file=out_file)

