import os

input = "test.in"
#input = "a-small.in";
#input = "a-large.in";
#input = "A-large.in"
input = "A-small-attempt0.in"

output = input.replace(".in", ".out")

in_f = open(input, "r")

def get_line():
	return in_f.readline()[:-1]
	
def get_int():
	return int(get_line())

def get_sep():
	return get_line().split(" ")
	
def get_sep_int():
	return [int(i) for i in get_sep()]	

def get_solution_str():
	line1 = get_int()
	for i in xrange(line1 - 1):
		get_line()
	opts1 = get_sep_int()
	for i in xrange(4 - line1):
		get_line()
	line2 = get_int()
	for i in xrange(line2 - 1):
		get_line()
	opts2 = get_sep_int()
	for i in xrange(4 - line2):
		get_line()
	match = [a for a in opts1 if a in opts2]
	if len(match) == 0:
		return "Volunteer cheated!"
	if len(match) > 1:
		return "Bad magician!"
	return match[0]

num_cases = get_int()
out = open(output, "w")

for cur_case in xrange(1, num_cases + 1):
	print cur_case
	sol = get_solution_str()
	
	out.write("Case #%d: %s\n" %(cur_case, sol))