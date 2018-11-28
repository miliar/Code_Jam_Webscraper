from __future__ import print_function
import sys
import time

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
	k = int(line[-1])
	pans = line[0]
	counter = 0
	while len(pans) >= k:
		if pans[0] == "+":
			pans = pans[1:]
		if pans[0] == "-" and len(pans) >= k:
			pans = flip(pans[:k]) + pans[k:]
			counter += 1
	
	if len(pans) == k-1 and pans == "+" * (k-1):
		return str(counter) 
	else:
		return "IMPOSSIBLE"

def flip(pans_line):
	flipper = lambda x : "+" if x == "-" else "-"
	return "".join(map(flipper, pans_line))


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Not enough args!")
	else:
		input_name = sys.argv[1]
		file_cont = read_file(input_name)	

		output_name = input_name[:input_name.index(".")] + ".out"
		handle_input(file_cont, output_name)	

