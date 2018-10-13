#!/usr/bin/python
import sys
import re

def read_input(input):
	num_list = map(int, input.readline().split(" "))
	L = num_list[0]
	D = num_list[1]
	num_cases = num_list[2]
	
	words = []
	for i in range(D):
		words.append(input.readline())
		
	cases = []
	for i in range(num_cases):
		cases.append(input.readline())
		
	return [words, cases]
	
if __name__ == "__main__":
	filename = sys.argv[1]
	file = open(filename)
	word_case_list = read_input(file)
	
	words = word_case_list[0]
	cases = word_case_list[1]
	
	case_num = 1
	for pattern in cases:
		match = 0
		
		p1 = pattern.replace("(", "[")
		p2 = p1.replace(")", "]")
		
		for w in words:
			if re.search(p2, w):
				match += 1
		
		print "Case #" + str(case_num) + ": " + str(match)
		case_num += 1
	
