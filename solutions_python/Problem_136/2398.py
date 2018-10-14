__author__ = 'donlnz'

import numpy as np

def solve_problem(filename, callback, n_lines_case):
	with open(filename) as file:
		n_cases = int(file.readline())
		for i in range(n_cases):
			case = []
			for j in range(n_lines_case):
				case.append(file.readline()[:-1].split(' '))
			yield(callback(case))

def problem_2_callback(case):
	case = case[0]
	c, f, x = float(case[0]), float(case[1]), float(case[2])
	return calc_min_time(c, f, x, 2)

def calc_min_time(c, f, x, i):
	'''
		c = farm cost
		f = farm cookies/s increase
		x = target number of cookies
		i = current cookies/s
	'''
	time = 0

	while True:
		dont_buy = (x / i)
		buy = (c / i) + (x / (i + f))

		if dont_buy < buy:
			return time + dont_buy
		else:
			time += (c / i)
			i += f

case_n = 1
with open('../output/p2.txt', 'w') as file:
	for i in solve_problem('../input/p2large.in', problem_2_callback, 1):
		file.write('Case #{}: {}\n'.format(case_n, i))
		#print('Case #{}: {}\n'.format(case_n, i))
		case_n += 1
