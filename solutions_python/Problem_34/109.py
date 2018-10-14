# *-* encoding: UTF-8 -*-
import sys

def split_testcase(test_case):
	testcase_splitted = []
	temp_list = []
	parenthesis_flag = False
	for character in test_case:
		if character == "(":
			parenthesis_flag = True
		elif character == ")":
			testcase_splitted.append(tuple(temp_list))
			temp_list = []
			parenthesis_flag = False
		elif parenthesis_flag:
			temp_list.append(character)
		else:
			temp_list.append(character)
			testcase_splitted.append(tuple(temp_list))
			temp_list = []
	return tuple(testcase_splitted)

def find_K(test_case, alien_words):
	K = 0;
	testcase_splitted = split_testcase(test_case)
	for word in alien_words:
		for pos, character in enumerate(word):
			if not character in testcase_splitted[pos]:
				break
			if pos == len(word)-1:
				K = K + 1
	return K
			
if __name__ == "__main__":
	FILENAME = "A-large.in"

	lines = file(FILENAME).read().splitlines()
	firstline = lines[0]
	(L, D, N) = map(int, firstline.split())

	alien_words = lines[1:D+1]
	test_cases = lines[D+1:]

	for i, test_case in enumerate(test_cases):
		if i == N-1:
			sys.stdout.write("Case #%d: %d" % (i+1, find_K(test_case,
							alien_words)))
		else:
			print "Case #%d: %d" % (i+1, find_K(test_case, alien_words))

