from __future__ import print_function

A = 10

def main(inputf, outputf):
	outf = file(outputf, 'w')
	with open(inputf, 'r') as f:
		lines = f.read().split('\n')

		for n in xrange(int(lines[0])):
			s1 = set(lines[(n * A) + 1 + int(lines[(n * A) + 1])].split())
			s2 = set(lines[(n * A) + 6 + int(lines[(n * A) + 6])].split())

			intersection = s1 & s2

			if len(intersection) == 1:
				print('Case #{}: {}'.format(n + 1, ''.join(intersection)), file=outf)
			elif len(intersection) == 0:
				print('Case #{}: Volunteer cheated!'.format(n+1), file=outf)
			else:
				print('Case #{}: Bad magician!'.format(n+1), file=outf)


if __name__ == '__main__':
	main('A-small-attempt0.in', 'result.out')