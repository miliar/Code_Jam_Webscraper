import random
import time

import numpy as np

res_path = "../../../../downloads/"

def solve_line(line):
	n = int(line)
	L = len(line)
	candidates = {line}
	for index in range(L):
		if int(line[index]) > 0:
			s = line[:index] + str(int(line[index])-1) + "9"*(L-index-1)
			candidates.add(s)
	solutions = set(candidates)
	for s in candidates:
		for i in range(1,L):
			if int(s[i]) < int(s[i-1]):
				solutions.remove(s)
				break
	return max(int(it) for it in solutions)
	

def mymain():
	input_name = "B-large"
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
