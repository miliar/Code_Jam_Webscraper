# uses python3.5
# uses libraries numpy, scipy, sympy, networkx, matplotlib
# you can install them with 'pip3 install <library-name>'
import random
import time

import numpy as np

res_path = "../../../../downloads/"


def solve(R, C, lines):
	grid = np.zeros((R, C), dtype=np.int32)
	coords = []
	for y in range(R):
		for x in range(C):
			grid[y, x] = ord(lines[y][x])
			if lines[y][x] != '?':
				coords.append((y, x))
	for y, x in coords:
		x_min, x_max = x, x
		y_min, y_max = y, y
		while x_min > 0 and np.all(grid[y, x_min - 1] == ord('?')):
			x_min -= 1
		while x_max < C - 1 and np.all(grid[y, x_max + 1] == ord('?')):
			x_max += 1
		while y_min > 0 and np.all(grid[y_min-1, x_min:x_max+1] == ord('?')):
			y_min -= 1
		while y_max < R-1 and np.all(grid[y_max+1, x_min:x_max+1] == ord('?')):
			y_max += 1
		grid[y_min:y_max+1, x_min:x_max+1] = grid[y,x]
	res = ""
	for y in range(R):
		for x in range(C):
			res += chr(grid[y,x])
		res += "\n"
	return res


def mymain():
	input_name = "A-large"
	output = open(res_path + input_name + ".out", "w")
	input_lines = open(res_path + input_name + ".in").readlines()
	input_lines = [line.strip() for line in input_lines]
	T = int(input_lines[0])
	input_lines = input_lines[1:]
	for i in range(1, T + 1):
		R, C = map(int, input_lines[0].split())
		lines = input_lines[1:R + 1]
		input_lines = input_lines[R + 1:]
		res = solve(R, C, lines)
		output.write("Case #{}:\n".format(i))
		output.write(res)


if __name__ == "__main__":
	print("starting...")
	start = time.time()
	random.seed(0)
	np.random.seed(0)
	mymain()
	end = time.time()
	print("elapsed time: {:.5f}s".format(end - start))
