import sys

DEBUG = 0
rl = sys.stdin.readline

def string_to_ints(str):
	return [int(num) for num in str.strip().split(' ')]

def read_lawn():
	dims = string_to_ints(rl())
	lines = [string_to_ints(rl()) for i in xrange(0, dims[0])]
	return dims, lines

def solve(dims, plans):
	n, m = dims
	rows = [plan for plan in plans]
	columns = [plan for plan in zip(*plans)]
	for i in xrange(0, n):
		for j in xrange(0, m):
			if DEBUG:
				print "Checking (%d,%d):" % (i,j)
				print "\tRow %d: %s" % (i+1, rows[i])
				print "\tColumn %d: %s" % (j+1, columns[j])
			if max(rows[i]) > plans[i][j] and max(columns[j]) > plans[i][j]:
				return 'NO'
	return 'YES'

def main():
	numcases = int(rl())
	for case in xrange(1, numcases+1):
		dims, plans = read_lawn()
		if DEBUG:
			print "Dimensions: %d x %d" % (dims[0], dims[1])
			print "Plans:"
			for plan in plans:
				print "\t%s" % plan

		answer = solve(dims, plans)
		print "Case #%d: %s" % (case, answer)

if __name__ == '__main__':
	main()