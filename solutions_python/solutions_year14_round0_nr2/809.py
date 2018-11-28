import os
import pdb

INPUT_FILE_NAME = "test.in"
#INPUT_FILE_NAME = "a-small.in";
#INPUT_FILE_NAME = "a-large.in";
#INPUT_FILE_NAME = "A-large.in"
INPUT_FILE_NAME = "B-small-attempt1.in"
INPUT_FILE_NAME = "B-large.in"

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

MAX_DEPTH = 300000
def get_solution_str():
	cost, farm_prod, target = get_sep_float()
	cur_prod = 2.0
	best_time = target / cur_prod
	time_till_here = 0.0
	for i in xrange(MAX_DEPTH):
		time_till_here += (cost/cur_prod)
		cur_prod += farm_prod
		best_time = min(best_time, time_till_here + target / cur_prod)
	return str(best_time)

num_cases = get_int()
out_f = open(OUTPUT_FILE_NAME, "w")

for cur_case in xrange(1, num_cases + 1):
	print "case", cur_case
	sol = get_solution_str()
	
	out_f.write("Case #%d: %s\n" %(cur_case, sol))