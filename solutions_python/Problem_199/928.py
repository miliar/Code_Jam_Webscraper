# Google Code Jam practice problems

import random as r

#file_in = "test.txt"
file_in = "A-small-attempt0.in"
#file_in = "A-large-practice.in"

file_out = "output.txt"

def answer(test_input):
	test_input = test_input.split()
	pancakes = list(test_input[0])
	len_spatula = int(test_input[1])
	print(pancakes, len_spatula)
	
	flips = 0
	for i in range(0, len(pancakes) - len_spatula + 1):
		if pancakes[i] == "-":
			flips += 1
			for j in range(i, i + len_spatula):
				if pancakes[j] == "+":
					pancakes[j] = "-"
				else:
					pancakes[j] = "+"
	if test_valid(pancakes):				
		print(pancakes, "with", flips, "flips")
		return flips
	else:
		print("IMPOSSIBLE")
		return "IMPOSSIBLE"
	
def get_random_pancakes(n):
	pancakes = []
	for i in range(n):
		num = r.randint(0,1)
		if num == 0:
			pancakes.append("+")
		else:
			pancakes.append("-")
	return pancakes
	
def test_valid(pancakes):
	for pancake in pancakes:
		if pancake == "-":
			return False
	return True

	
def write_file():
	f = open(file_in)
	out = open(file_out, "w")
	num_cases = int(f.readline())
	for i in range(num_cases):
		test_input = f.readline().strip()
		output = answer(test_input)
		out.write("Case #" + str(i+1) + ": " + str(output) + "\n")
		print("Case #" + str(i+1) + ": " + str(output))
		print()
	f.close()
	out.close()
	
write_file()