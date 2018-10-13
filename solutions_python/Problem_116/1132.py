import sys
from array import array

file_string = sys.argv[1]
my_file = open (file_string)
current_line = my_file.readline()
n = int(current_line,10)

def construct():
	my_list = []
	m = 16
	full = True
	while m > 0:
		current = my_file.read(1)
		if current == ".":
			full = False
		if not current == "\n":
			my_list.append(current)
			m = m- 1
	return full, my_list
def check_result(x, o, t):
	if t == 0:
		if x == 4:
			return "X"
		elif o == 4:
			return "O"
		else:
			return "none"
	elif t == 1:
		if x == 3:
			return "X"
		elif o == 3:
			return "O"
		else: 
			return "none"
	else:
		return "none"	
def checkrow(my_list, n):
	start = 4*n
	end = start+4
	x = 0
	o = 0
	t = 0
	while start < end:
		current = my_list[start]
		if current == "X":
			x = x+1
		elif current == "O":
			o = o+1
		elif current == "T":
			t = t+1
		start = start + 1

	output = check_result(x,o,t)

	return output
def checkcol(my_list,n):

	start = n
	end = start + 13
	x = 0
	o = 0
	t = 0
	while start < end:
		current = my_list[start]

		if current == "X":
			x = x+1
		elif current == "O":
			o = o+1
		elif current == "T":
			t = t+1
		start = start + 4

	output = check_result(x,o,t)

	return output
def check_diagonal(my_list):
	one = [0,5,10,15]
	two = [3,6,9,12]
	x = 0
	o = 0
	t = 0
	for y in one:
		current = my_list[y]
		if current == "X":
			x = x+1
		elif current == "O":
			o = o+1
		elif current == "T":
			t = t+1
	result = check_result(x,o,t)
	if result == "none":
		x = 0
		t = 0
		o = 0
		for y in two:
			current = my_list[y]
			if current == "X":
				x = x+1
			elif current == "O":
				o = o+1
			elif current == "T":
				t = t+1
		result = check_result(x,o,t)
	return result
def process_list():
	full, my_list = construct()
	output = "none"
	if output == "none":
		output = checkrow(my_list, 0)
	if output == "none":
		output = checkrow(my_list, 1)
	if output == "none":
		output = checkrow(my_list, 2)
	if output == "none":
		output = checkrow(my_list, 3)
	if output == "none":
		output = checkcol(my_list, 0)
	if output == "none":
		output = checkcol(my_list, 1)
	if output == "none":
		output = checkcol(my_list, 2)
	if output == "none":
		output = checkcol(my_list, 3)
	if output == "none":
		output = check_diagonal(my_list)

	return full, output


m = 1
while (m <= n):
	full, output = process_list()

	if output == "none":
		if not full:
			print "Case #" + str(m) + ": " + "Game has not completed"
		else:
			print "Case #" + str(m) + ": " +"Draw"
	elif output == "X":
		print "Case #" + str(m) + ": " + "X won"
	elif output == "O":
		print "Case #" + str(m) + ": " + "O won"
	m = m+1