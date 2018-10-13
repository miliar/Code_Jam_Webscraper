#
# URL: http://code.google.com/codejam/contest/dashboard?c=351101#s=p0
#

import sys

# =====================================

def read_input(filename):

	lines = open(filename).readlines()

	line = lines[0]
	line.strip()
	num_of_testcase = int(line)
	lines = lines[1:]

	for i in range(num_of_testcase):

		line = lines[i].strip()
		items = line.split(" ")

		c = int(items[0])
		dict_combine = {}
		for j in range(c):
			s = items[j+1]
			k1 = s[0] + s[1]
			k2 = s[1] + s[0]
			dict_combine[k1] = s[2]
			dict_combine[k2] = s[2]

		d = int(items[c+1])
		dict_clear = {}
		for k in range(d):
			s = items[c+2]
			k1 = s[0] + s[1]
			k2 = s[1] + s[0]
			dict_clear[k1] = 1  # the val doesn't matter
			dict_clear[k2] = 1  # the val doesn't matter

		n = int(items[c+d+2])
		invoke_list_str = items[-1]

		solve_it(i+1, dict_combine, dict_clear, n, invoke_list_str)


# ------------------------------------

def print_debug(s):

	debug = 0
	if debug == 1:
		print s

# ------------------------------------

def apply_combine(s, dict):
	if len(s) < 2:
		return s
	else:
		last_2_ele = s[-2:]
		if dict.has_key(last_2_ele):
			val = dict[last_2_ele]
			s = s[:-2]
			s += val
			return s
		else:
			return s

# ------------------------------------

def apply_clear(s, dict):
	if len(s) < 2:
		return s
	else:
		last_ch = s[-1]
		for i in range(len(s)-1):
			ch = s[i]
			ch_2 = ch + last_ch
			if dict.has_key(ch_2):
				#s = s[0:i]
				s = ""
				return s
		return s

# ------------------------------------

def solve_it(test_num, dict_combine, dict_clear, n, invoke_list_str):

	print_debug("//=================================")
	print_debug(str(invoke_list_str))
	print_debug(str(dict_combine))
	print_debug(str(dict_clear))

	curr_list_str = ""
	for i in range(n):
		print_debug("//----------")
		curr_list_str += invoke_list_str[i]
		print_debug(curr_list_str)
		curr_list_str = apply_combine(curr_list_str, dict_combine)
		print_debug(curr_list_str)
		curr_list_str = apply_clear(curr_list_str, dict_clear)
		print_debug(curr_list_str)


	L = []
	for i in range(len(curr_list_str)):
		L.append(curr_list_str[i])
	sol = "[" + ", ".join(L) + "]"
	print "Case #" + str(test_num) + ": " + sol

# ------------------------------------

def main():
	#read_input("test.in")
	#read_input("B-small-attempt0.in")
	read_input("B-small-attempt1.in")
	#read_input("A-large-practice.in")


# ====================================

if __name__ == "__main__":
	main()

