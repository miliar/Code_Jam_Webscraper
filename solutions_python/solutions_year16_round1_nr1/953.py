import os
import sys
current = os.getcwd()
outer = os.path.dirname(os.getcwd())
sys.path.append(current)
sys.path.append(outer)

from utils.io import *

def main():
	start = time_in_ms()
	info = parse_data()
	raw_tests = info[0]
	output_file = info[1]
	results = []

	for idx, r_test in enumerate(raw_tests):
		print "Trying #"+str(idx)
		test = r_test[0]
		results.append(solve(test))

	data_output(results, output_file)
	print "Time taken:",str(time_in_ms() - start)+"ms"

def solve(test):
	word = test
	last_word = ""

	for c in word:
		if not last_word:
			last_word = c
		elif c >= last_word[0]:
			last_word = c + last_word
		else:
			last_word += c

	return last_word

if __name__ == '__main__':
	main()