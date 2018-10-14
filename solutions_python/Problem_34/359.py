#!/usr/bin/python
import string
import re
def read_input():
	file = open("input.in")
	lines = file.readlines()
	file.close()
	return lines

def write_output(lines):
	file = open("output.out", "w")
	file.writelines(lines)
	file.close()

def get_letter_groups(case):
	groups = re.findall("\((\w+)\)|(\w)", case)
	return [a or b for (a, b) in groups]

if __name__=="__main__":
	#print("reading input")
	input = read_input()
	output = []
	(L, D, N,) = input[0].split(" ")
	L = int(L)
	D = int(D)
	N = int(N)
	#print("letters = " + str(L))
	#print("words = " + str(D))
	#print("cases = " + str(N))
	words = input[1:D+1]
	#print("word list = " + str(words))
	cases = input[1+D:]
	for (case_num, case) in enumerate(cases):
		#print("case: " + str(case_num))
		groups = get_letter_groups(case[:-1])
		#print("groups: " + str(groups))
		num_words = 0
		for word in words:
			#print("word: " + str(word[:-1]))
			isgood = True
			#print("word list length: " + str(len(list(word[:-1]))))
			#print("groups length: " + str(len(groups)))
			for wordLetter, group in zip(list(word[:-1]), groups):
				if not wordLetter in group:
					isgood = False
			if isgood:
				num_words += 1
		#print("groups = " + str(groups))
		output.append("Case #" + str(case_num+1) + ": " + str(num_words) + "\n")
	write_output(output)
