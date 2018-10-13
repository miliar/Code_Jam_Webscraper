#!/usr/bin/env python

def main():
	infile = open('A-small-attempt0.in', 'r')
	outfile = open('cj-a-small-test.out', 'w')

	num_case = int(infile.readline())
	print num_case

	for i in range(0, num_case):
		choice_1 = int(infile.readline())
		for j in range(0, choice_1 - 1):
			infile.readline()
		row_1 = map(int, infile.readline().split(' '))
		for j in range(0, 4 - choice_1):
			infile.readline()
		print row_1

		choice_2 = int(infile.readline())
		for j in range(0, choice_2 - 1):
			infile.readline()
		row_2 = map(int, infile.readline().split(' '))
		for j in range(0, 4 - choice_2):
			infile.readline()
		print row_2

		card_list = []
		for c1 in row_1:
			for c2 in row_2:
				if c1 == c2:
					card_list.append(c1)
					if len(card_list) > 1:
						break

		outfile.write('Case #{0}: '.format(i + 1))
		if len(card_list) == 0:
			outfile.write('Volunteer cheated!')
		elif len(card_list) > 1:
			outfile.write('Bad magician!')
		else:
			outfile.write('{0}'.format(card_list[0]))
		outfile.write('\n')

	infile.close()
	outfile.close()

if __name__ == "__main__":
	main()