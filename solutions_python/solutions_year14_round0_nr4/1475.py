def split_line(line, sep=' ', reverse=False):
	numbers = []
	num = ''

	for char in line:
		if char == sep:
			if num != '':
				numbers.append(float(num))
			num = ''
		else:
			num += char

	if num != '':
		numbers.append(float(num))
	num = ''

	numbers.sort(reverse=reverse)

	return numbers

def war(naomi, ken, no):
	count = 0

	for x in xrange(no):

		if naomi[0] > ken[0]:
			if naomi[0] > ken[-1]:
				count += 1

			del naomi[0]
			del ken[-1]
		else:
			y = 0
			while naomi[0] < ken[y]:
				if y == len(ken) - 1:
					break
				y += 1

			del naomi[0]
			del ken[y-1]

	return count

def decietful_war(naomi, ken, no):
	count = 0

	for x in xrange(no):

		if naomi[-1] > ken[-1]:
			count += 1
			del naomi[-1]
			del ken[-1]
		else:
			del naomi[-1]
			del ken[0]

	return count


if __name__ == '__main__':
	f = open('in.in', 'r')#Open input file

	out = open('out.out', 'w')#Open output file

	test_cases = int(f.readline().strip())# Get number of test cases
	

	for n in xrange(1, test_cases+1):

		no = int(f.readline().strip())
		naomi = split_line(f.readline().strip(), reverse=True)
		ken = split_line(f.readline().strip(), reverse=True)

		n_war = war(naomi[:], ken[:], no)
		n_d_war = decietful_war(naomi, ken, no)

		case = 'Case #{0}: {1} {2}\n'.format(n, n_d_war, n_war)
		out.write(case)