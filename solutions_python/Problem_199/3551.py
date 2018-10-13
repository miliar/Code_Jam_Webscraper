#!/usr/bin/env python3

# from test import test


def last_index(l, value):
	for i, v in enumerate(reversed(l)):
		if v == value:
			return len(l) - 1 - i
	return -1


def is_happy(pancakes):
	return all(pancake == '+' for pancake in pancakes)


def flip(pancakes, start, n):
	while start + n > len(pancakes):
		start -= 1

	for i in range(start, start + n):
		pancakes[i] = '+' if pancakes[i] == '-' else '-'

	return pancakes


def make_happy(pancakes, flipper_size):
	flips = 0
	stacks = set()

	while not is_happy(pancakes):
		i = pancakes.index('-')
		flip(pancakes, i, flipper_size)
		stack = ''.join(pancakes)

		if stack in stacks:
			return 'IMPOSSIBLE'

		flips += 1
		stacks.add(stack)

	return flips


def run_task(line):
	pancakes, flipper_size = line.split()
	flipper_size = int(flipper_size)
	pancakes = list(pancakes)
	return make_happy(pancakes, flipper_size)


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
	test(run_task, 'A-large')
