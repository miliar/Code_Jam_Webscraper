import math
import sys

def solve_case_naive(radius, paint):
	lines = 0
	needed = radius * 2 + 1
	while paint >= needed:
		lines += 1
		paint -= needed
		radius += 2
		needed += 4
	return lines

def solve_case(radius, paint):
	needed = radius * 2 + 1
	if radius % 2 == 1:
		free_lines = (radius - 1) / 2
		extra_paint = 2*free_lines ** 2 + free_lines
		paint += extra_paint
		return int((math.sqrt(1 + 8*paint) - 1) / 4) - free_lines
	else:
		free_lines = radius / 2
		extra_paint = 2*free_lines**2 - free_lines
		paint += extra_paint
		return int((math.sqrt(1 + 8*paint) + 1) / 4) - free_lines

def main(input):
	data = map(lambda x: map(int, x.split()), input.split('\n'))
	num_cases, = data.pop(0)
	for i in xrange(num_cases):
		in_data = data.pop(0)
		print 'Case #{0}: {1}'.format(i + 1, solve_case(*in_data))
		#print 'Case #{0}: {1}'.format(i + 1, solve_case_naive(*in_data))


main(sys.stdin.read())