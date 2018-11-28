#! /usr/bin/python

__author__ = "assim"
__date__ = "$May 8, 2010 9:10:51 AM$"

import sys


def bin(s):
	return str(s) if s <= 1 else bin(s >> 1) + str(s & 1)

def solve(n, k):

	#state 0 OFF state
	#state 1 ON state

	bin_str = bin(k)
	print bin_str
	if len(bin_str) < n:
		return "OFF"
	elif "0" in bin_str[-n:]:
		return "OFF"
	else:
		return "ON"

def parse(p = "a-l"):
	input = open("%s-i" %(p), "r")
	output = open("%s-o"%(p), "w")
	output_str_list = []
	num_cases = int(input.readline())
	for case in xrange(num_cases):
		n, k = input.readline().split()
		output_str_list.append("Case #%s: %s" % (case + 1, solve(int(n), int(k))))
		#output.write("Case #%s: %s" % (case + 1, solve(int(n), int(k))))
		#output.write("\n")
	input.close()
	output.write("\n".join(output_str_list))
	output.close()







if __name__ == "__main__":
	parse()
	#print solve(1,1)
	#print solve(4,47)

