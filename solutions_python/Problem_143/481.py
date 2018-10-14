

def main(fname='test.in', out_fname='test.out'):

	out_file = open(out_fname, 'w')

	with open(fname, 'r') as in_file:
		rows = in_file.read().split('\n')

		for n in xrange(1, int(rows[0]) + 1):
			row = rows[n]
			a, b, c = map(int, row.split())
			out_file.write('Case #{}: {}\n'.format(n, z(a, b, c)))

	out_file.close()

def z(a, b, c):
	count = 0
	for n in range(a):
		for o in range(b):
			if int(bin(n&o),2) < c:
				count += 1

	return count


if __name__ == '__main__':
	#main()
	main('B-small-attempt0.in', 'B-small.out')

