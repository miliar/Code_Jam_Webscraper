import numpy as np
from math import floor

def make_answer(_n):
	if _n%2 ==0:
		return ' '.join([str(_n/2), str(_n/2-1)])
	else:
		return ' '.join([str(_n/2), str(_n/2)])

def solve(n, k):
	if k==1:
		return make_answer(n)

	# else, calc d, where 2^d <= k < 2^(d+1)
	d = int(floor(np.log2(k)))
	n_left = n - 2**d + 1
	n_left_div = n_left / (2**d)
	n_left_mod = n_left % 2**d

	order = k - 2**d
	if order < n_left_mod:
		return make_answer(n_left_div + 1)
	else:
		return make_answer(n_left_div)

if __name__ == '__main__':
	with open('C-small-2-attempt0.in', 'r') as f1:
		with open('output3.txt', 'w') as f2:
			lines = f1.readlines()
			num_test = int(lines[0])
			case = 1
			for line in lines[1:]:
				n, k = [int(x) for x in line.strip().split()]
				answer = solve(n, k)
				f2.write('Case #{}: {}\n'.format(case, answer))
				case += 1
