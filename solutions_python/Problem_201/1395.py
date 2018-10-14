from __future__ import print_function
import sys
import time
import math

def read_file(fn):
	with open(fn) as f:
		cont = f.readlines()
	print("Read input file \"" + fn + "\" successfully!")	
	return [line.strip().split(" ")  for line in cont]

def handle_input(fc, out_name):
	output_file = open(out_name, 'w')
	print("Opened output file \"" + out_name + "\" successfully!")
	test_cases_count = int(fc[0][0])
	
	for test_index in range(1, test_cases_count + 1):
		print("Case #" + str(test_index) + "... ", end = '')
		result = handle_line(fc[test_index])
		output_file.write("Case #" + str(test_index) + ": " + result + "\n")
		print("Done")
	output_file.close()
	return

def handle_line(line):
	N = int(line[0])
	K = int(line[1])
	
	return solve(N, K)

def solve(N, K):
	print(str((N,K)))
	if K == 1:
		return str(int(math.ceil((N - 1) / 2.0))) + " " + str(int(math.floor((N - 1) / 2.0)))

	if N % 2 == 1:
		return solve((N-1) / 2, int(math.ceil((K - 1) / 2.0)))
	if N % 2 == 0 and K % 2 == 1:
		return solve(N / 2 - 1, (K - 1) / 2)
	if N % 2 == 0 and K % 2 == 0:
		return solve(N / 2, K / 2)

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Not enough args!")
	else:
		input_name = sys.argv[1]
		file_cont = read_file(input_name)	

		output_name = input_name[:input_name.index(".")] + ".out"
		handle_input(file_cont, output_name)	

