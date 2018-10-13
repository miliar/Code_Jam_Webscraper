#!/usr/bin/env python3


def is_tidy(n):
	digits = list(str(n))
	digits.sort()
	return ''.join(digits) == str(n)


def run_task(line):
	n = int(line)

	while n > 0:
		if is_tidy(n):
			return n
		n -= 1

	return 1


def test(func, filename):
	input_file = open('tests/' + filename + '.in')
	output_file = open('tests/' + filename + '.out', 'w')
	lines = input_file.readlines()

	cases = int(lines[0])
	for case in range(1, cases + 1):
		line = lines[case].strip()
		result = func(line)
		print('Case #{}: {}'.format(case, result), file=output_file)


if '__main__' == __name__:
	test(run_task, 'B-small-attempt0')
