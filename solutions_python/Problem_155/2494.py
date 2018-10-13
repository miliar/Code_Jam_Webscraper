from sys import argv


def main(input):
	cases = []
	with open(input, 'r') as f:
		cases = f.readlines()
	with open('output', 'w') as fout:
		for index, val in enumerate(cases[1:]):

			val = val.replace('\n', '')

			max_shyness = int(val.split(" ")[0])
			shyness = [int(i) for i in val.split(" ")[1:][0]]

			standing = index
			friends = 0
			for i in xrange(max_shyness+1):
				total = sum(shyness)
				standing = sum(shyness[:i if i else 0])
				if standing < i:
					friends += 1
					shyness[i] += 1
			fout.write('Case #%d: %d\n' % (index + 1, friends))


if __name__ == '__main__':
	if len(argv) == 2:
		main(argv[1])
	else:
		main('input')
