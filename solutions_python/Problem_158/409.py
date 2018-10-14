# -*- coding: utf-8 -*-

import pdb

def could_win(x, r, c):
	if r > c:
		r, c = c, r

	if x == 1:
		return False
	if x >= 7:
		return True
	if r * c % x != 0:
		return True
	if max(r, c) < x:
		return True
	min_length_list = [0, 1, 1, 2, 2, 3, 3]
	if min(r, c) < min_length_list[x]:
		return True
	if x == 4:
		if r == 2 and c == 4:
			return True
	if x == 5:
		if r == 3 and c == 5:
			return True
		if r == 4 and c == 5:
			return False
	if x == 6:
		if r == 3 and c == 6:
			return True

	return False


def main():
	# pdb.set_trace()

	input_file = 'D-small-attempt0.in.txt'
	output_file = 'out'
	output_format = 'Case #{0}: {1}\n'

	results = []

	with open(input_file, 'r') as f:
		case_total = str_to_int(f.readline())
		# for each case:
		for i in range(case_total):
			X, R, C = str_to_int_list(f.readline())
			if could_win(X, R, C):
				results.append('RICHARD')
			else:
				results.append('GABRIEL')
			
	with open(output_file, 'w') as f:
		for i in range(len(results)):
			# for each result
			f.write(output_format.format(i+1, results[i]))	


# --------------------------------------------

def str_to_int(s):
	return int(s.strip())

def str_to_int_list(s):
	return [int(x) for x in s.strip().split()]

if __name__ == '__main__':
	main()



