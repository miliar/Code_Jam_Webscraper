import random
import time
from collections import Counter, defaultdict

import numpy as np

res_path = "../../../../downloads/"

def solve_line(line):
	n,k = line.split(" ")
	n,k = int(n), int(k)
	s = defaultdict(int)
	s[n] = 1
	for _ in range(k-1):
		m = max(s.keys())-1
		s[m+1] -= 1
		if s[m+1] == 0:
			s.pop(m+1)
		s[m//2] += 1
		s[m - m//2] += 1
	m = max(s)-1
	return "{} {}".format(m - m // 2, m//2)
	

def mymain():
	input_name = "C-small-2-attempt0"
	output = open(res_path + input_name + ".out", "w")
	input_lines = open(res_path + input_name + ".in").readlines()
	input_lines = input_lines[1:]
	input_lines = [line.strip() for line in input_lines]
	for i, line in enumerate(input_lines):
		solution = solve_line(line)
		output_line = "Case #{}: {}\n".format(i+1, solution)
		output.writelines(output_line)
		print(output_line, end="")
	
	


if __name__ == "__main__":
	print("starting...")
	start = time.time()
	random.seed(0)
	np.random.seed(0)
	mymain()
	end = time.time()
	print("elapsed time: {:.5f}s".format(end - start))
