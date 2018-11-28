from collections import deque
import heapq
from heapq import heappop, heappush
import sys
import multiprocessing

def read_in(pipe):
    lines = pipe.readlines()
    for i in xrange(len(lines)):
        lines[i] = lines[i].replace('\n','')
    return lines

class ProblemSet(object):
	problem_set = []

def main(args):
	ProblemSet.problem_set = read_in(open(args)) 
	n_test_cases = int(ProblemSet.problem_set[0])
	# pool = multiprocessing.Pool(processes=4)
	# aggregate = pool.map(solve, range(n_test_cases))
	# pool.close()
	# pool.join()
	# for result in aggregate:
	# 	print result
	for test_case in xrange(n_test_cases):
		print real_solve(test_case)

def real_solve(test_case):
	problem = ProblemSet.problem_set[test_case+1]
	cook_line, k = problem.split(' ')
	cook_line = [0 if c == '-' else 1 for c in cook_line]
	k = int(k)

	# if k == len(cook_line):
	# 	min_flips = brute_force_solve(cook_line, k)
	# else:
	# 	try:
	# 		min_flips = divide(cook_line, k)
	# 	except TypeError:
	# 		min_flips = 'IMPOSSIBLE'

	min_flips = 0
	while cook_line.count(0):
		try:
			anchor = len(cook_line) - cook_line[::-1].index(0) - 1
		except ValueError:
			break
		if (anchor - k + 1) < 0:
			min_flips = 'IMPOSSIBLE'
			break
		for swap_index in xrange(anchor - k + 1, anchor + 1):
			cook_line[swap_index] ^= 1

		min_flips +=1

		if all(cook_line):
			break

	return 'Case #{0}: {1}'.format(test_case + 1, min_flips)

def divide(cook_line, k):
	if len(cook_line) <= k or len(cook_line) < 5:
		return brute_force_solve(cook_line, k)

	mid = len(cook_line) / 2
	l = divide(cook_line[:mid], k)
	r = divide(cook_line[mid+1:], k)
	mid_flips = 0

	if not isinstance(l, int):
		l = brute_force_solve(cook_line[:mid+1], k)
		if not isinstance(l, int):
			raise TypeError

	elif not isinstance(r, int):
		r = brute_force_solve(cook_line[mid:], k)
		if not isinstance(r, int):
			raise TypeError
	else:
		l = 0
		r = 0
		mid_flips = brute_force_solve(cook_line[mid-(k/2):mid+(k/2)], k)
		if not isinstance(mid_flips, int):
			raise TypeError

	total = l+r+mid_flips
	return total

def brute_force_solve(cook_line, k):
	if all(cook_line):
		return 0

	if k == len(cook_line):
		if not any(cook_line):
			return 1
		else:
			return 'IMPOSSIBLE'
	elif k < len(cook_line):
		visited = set()
		cook_line = tuple(cook_line)
		queue = []
		heappush(queue, (0, cook_line))
		heapq.heapify(queue)
		unique_nodes = set()

		n_flips = 0
		found_sol = False
		while queue:
			# print queue
			curr = heappop(queue)
			# print curr
			path_length, cook_line = curr

			if all(cook_line):
				found_sol = True
				n_flips = path_length
				break
			elif path_length > len(cook_line) - k + 1:
				#impossible situation
				found_sol = False
				break
			# print neighbors(curr, k)
			for nb in neighbors(curr, k):
				if nb[1] not in visited:
					heappush(queue, (nb[0] + path_length, nb[1]))
			
			visited.add(cook_line)
			n_flips +=1

		if not found_sol:
			return 'IMPOSSIBLE'
		else:
			return n_flips

	else:
		return 'IMPOSSIBLE'

def neighbors(bits, flip_size):
	length, path = bits
	nbs = set()
	for i in xrange(len(path) - flip_size + 1):
		flipped = tuple(path[0:i]) + tuple(map(lambda x: x ^ 1, path[i:i+flip_size])) + tuple(path[i+flip_size:])
		nbs.add((1, flipped))
	return nbs

def test_sol_and_output_results(input_file, write_to):
	f = open(input_file, 'r')
	out_f = open(write_to, 'w')
	sys.stdout = out_f
	sys.stdin = f
	main()
	f.close()
	out_f.close()

def verify_correct_output(outfile, ground_truth_file):
	with open(outfile, 'r') as f1:
		with open(ground_truth_file, 'r') as f2:
			print f1.read() == f2.read()

			
if __name__ == "__main__":
	input_file = 'A-large.in'
	main(input_file)