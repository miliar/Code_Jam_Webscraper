import sys

def main(argv):
	filename = argv[1]
	output = argv[2]
	with open(filename) as f:
		with open(output, 'w+') as out:
			num_tests = int(f.readline())
			for test in range(num_tests):
				first_ans = int(f.readline())
				lines = [[] for i in range(4)]
				for i in range(4):
					lines[i] = f.readline().split()
				second_ans = int(f.readline())
				lines2 = [[] for i in range(4)]
				for i in range(4):
					lines2[i] = f.readline().split()
				possibilities = [i for i in lines[first_ans - 1] if i in lines2[second_ans - 1]]
				out.write('Case #{}: '.format(test + 1))
				if len(possibilities) == 1:
					out.write('{}\n'.format(possibilities[0]))
				elif len(possibilities) == 0:
					out.write('Volunteer cheated!\n')
				elif len(possibilities) > 1:
					out.write('Bad magician!\n')

		


main(sys.argv)

