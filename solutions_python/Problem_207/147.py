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
	
	counting_index = 1
	for test_index in range(1, test_cases_count + 1):
		print("Case #" + str(test_index) + "... ", end = '')

		next_length = 1
		result = handle_line(fc[counting_index:counting_index + next_length])
		
		counting_index += next_length
		output_file.write("Case #" + str(test_index) + ": " + result + "\n")
		print("Done")
	output_file.close()
	return

def handle_line(lines):
	N,R,O,Y,G,B,V = tuple(map(int, lines[0]))
	print(N,R,O,Y,G,B,V)

	if N == 1:
		if O == 1:
			return "O"
		if G == 1:
			return "G"
		if V == 1:
			return "V"
		if R == 1:
			return "R"
		if Y == 1:
			return "Y"
		if B == 1:
			return "B"

	# to_add = ["R"] * R + ["O"] * O + ["Y"] * Y + ["G"] * G + ["B"] * B + ["V"] * V

	if (N == R + G or N == Y + V or N == B + O):
		return handle_two_types(N,R,O,Y,G,B,V)

	if not (\
		(B >= O + 1 or O == 0) \
		and \
		(Y >= V + 1 or V == 0) \
		and \
		(R >= G + 1 or G == 0)):
		return "IMPOSSIBLE"

	to_add = []
	if O > 0:
		to_add.append("BO" * O + "B")
		to_add += ["B"] * (B - (O + 1))
	else:
		to_add += ["B"] * B
	if V > 0:
		to_add.append("YV" * V + "Y")
		to_add += ["Y"] * (Y - (V + 1))
	else:
		to_add += ["Y"] * Y
	if G > 0:
		to_add.append("RG" * G + "R")
		to_add += ["R"] * (R - (G + 1))
	else:
		to_add += ["R"] * R

	return handle_three_types(to_add)

def get_nums(lst):
	R = 0
	Y = 0
	B = 0
	for elem in lst:
		if elem[0] == "R":
			R += 1
		if elem[0] == "Y":
			Y += 1
		if elem[0] == "B":
			B += 1
	return (R,Y,B)

def handle_two_types(N,R,O,Y,G,B,V):
	if N == R + G and R == G:
		return "RG" * R
	if N == Y + V and Y == V:
		return "YV" * Y
	if N == B + O and B == O:
		return "BO" * B
	return "IMPOSSIBLE"

def handle_three_types(lst):
	print("3 types")
	reds = []
	blues =[]
	yellows = []

	for elem in lst:
		if elem[0] == "R":
			reds.append(elem)
		if elem[0] == "B":
			blues.append(elem)
		if elem[0] == "Y":
			yellows.append(elem)

	R,Y,B = len(reds), len(yellows), len(blues)

	l = sorted([reds, yellows, blues], key = lambda x : len(x))
	print(l)
	small = l[0]
	medium = l[1]
	large = l[2]

	print(len(large), len(medium), len(small))

	if len(medium) == 0 and len(small) == 0:
		print("2 zeros")
		if len(large) == 1:
			return large[0]
		else:
			return "IMPOSSIBLE"


	# # just 1 type, must be 1 of it
	# if R == 0 and Y == 0:
	# 	if B == 1:
	# 		return blues[0]
	# 	else:
	# 		return "IMPOSSIBLE"
	# if R == 0 and B == 0:
	# 	if Y == 1:
	# 		return yellows[0]
	# 	else:
	# 		return "IMPOSSIBLE"
	# if B == 0 and Y == 0:
	# 	if R == 1:
	# 		return reds[0]
	# 	else:
	# 		return "IMPOSSIBLE"


	if len(small) == 0:
		print("1 zero")
		if len(large) == len(medium):
			return "".join(map(lambda x : x[0] + x[1], zip(large, medium)))
		else:
			return "IMPOSSIBLE"

	# ## 2 types
	# if R == 0:
	# 	if Y == B:
	# 		return "".join(map(lambda x : x[0] +x[1], zip(yellows, blues)))
	# if Y == 0:
	# 	if R == B:
	# 		return "".join(map(lambda x : x[0] +x[1], zip(reds, blues)))
	# if B == 0:
	# 	if Y == R:
	# 		return "".join(map(lambda x : x[0] +x[1], zip(yellows, reds)))


	print("0 zeros")
	if len(medium) + len(small) < len(large):
		return "IMPOSSIBLE"
	else: # enough space
		if len(small) + len(medium) == len(large): # exactly fits
			small_medium = small + medium
			return "".join(map(lambda x : x[0] + x[1], zip(large, small_medium)))
		else:
			delta = len(small) + len(medium) - len(large)
			medium_s = medium[:-delta]
			small_s = small[:-delta]

			small_medium_e = map(lambda x : x[0] + x[1], zip(medium[-delta:], small[-delta:]))

			small_medium = small_medium_e + small_s + medium_s
			return "".join(map(lambda x : x[0] + x[1], zip(large, small_medium)))

	# ## 3 types
	# if R > Y and R > B: # r is max
	# 	if Y + B >= R: # enough space!
	# 		if Y
	# 	else:
	# 		return "IMPOSSIBLE"
	# if Y > R and Y > B: # y max
	# 	if R + B >= Y: # enough space
	# 		## TODO
	# 	else:
	# 		return "IMPOSSIBLE"
	# if B > R and B > Y: # b is max
	# 	if R + Y >= B: # enough space
	# 		## TODO
	# 	else:
	# 		return "IMPOSSIBLE"


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Not enough args!")
	else:
		input_name = sys.argv[1]
		file_cont = read_file(input_name)	

		output_name = input_name[:input_name.index(".")] + ".out"
		handle_input(file_cont, output_name)	

