import os

INPUT_FILE_NAME = "test.in"
INPUT_FILE_NAME = "D-large.in"

OUTPUT_FILE_NAME = INPUT_FILE_NAME.replace(".in", ".out")
in_f = open(INPUT_FILE_NAME, "r")

def get_line():
	return in_f.readline()[:-1]

def get_int():
	return int(get_line())

def get_float():
	return float(get_line())

def get_sep():
	return get_line().split(" ")

def get_sep_int():
	return [int(i) for i in get_sep()]

def get_sep_float():
	return [float(i) for i in get_sep()]

def solve_normal(my, his):
	res = 0
	for i in xrange(len(my)):
		my_play = max(my)
		if my_play > max(his):
			his_play = min(his)
			res += 1
		else:
			his_play = min([a for a in his if a > my_play])
		my.remove(my_play)
		his.remove(his_play)
	return res

def solve_cheat(my, his):
	my=sorted(my)
	his=sorted(his)
	res = 0
	for i in xrange(len(my)):
		#print "My-----\t" + str(my) + "My"
		#print "His\t" + str(his) + "His"
		if my[0] > his[-1]:
			return res + len(my)
		if my[-1] < his[0]:
			return res
		my_play = min([a for a in my if a > his[0]])
		res += 1
		my.remove(my_play)
		his = his[1:]

	return 0

def get_solution_str():
	_ignore = get_int()
	my = get_sep_float()
	his = get_sep_float()
	my2 = [a for a in my]
	his2 = [a for a in his]
	return "%d %d" % (solve_cheat(my, his), solve_normal(my2, his2))	

num_cases = get_int()
out_f = open(OUTPUT_FILE_NAME, "w")

for cur_case in xrange(1, num_cases + 1):
	print "case", cur_case
	sol = get_solution_str()
	
	out_f.write("Case #%d: %s\n" %(cur_case, sol))