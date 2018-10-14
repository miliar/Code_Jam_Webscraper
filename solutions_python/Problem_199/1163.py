import sys

def flip(row, idx, count):
	for i in xrange(idx, idx+count):
		if row[i] == '-':
			row[i] = '+'
		else:
			row[i] = '-'


def solve(row, k):
	row = list(row)

	pos = 0
	count = 0

	while pos < len(row)-k+1:
		if row[pos] == '-':
			count += 1
			flip(row, pos, k)
		pos += 1

	if len(set(row)) != 1:
		return 'IMPOSSIBLE'

	return count

def main():
	f = open(sys.argv[1], 'rb')

	tests = int(f.readline().strip())

	ret = []
	for test in xrange(tests):
		row, k = f.readline().strip().split()
		k = int(k)
		ret.append(solve(row, k))

	for i, flips in enumerate(ret):
		print "Case #{}: {}".format(i+1, flips)


if __name__ == '__main__':
	main()