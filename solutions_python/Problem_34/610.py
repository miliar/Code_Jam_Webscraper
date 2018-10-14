import sys
import re

if __name__ == "__main__":
	lines = sys.stdin.read().split("\n")
	
	params = lines[0].split(" ")
	L = int(params[0])
	D = int(params[1])
	N = int(params[2])
	
	word_section = lines[1:D+1]
	test_section = lines[D+1:N+D+1]
	
	# words list
	alien_words = []
	for word in word_section:
		alien_words += [word,]
	
	testIndex = 0
	for test in test_section:
		testIndex += 1
		num_matches = 0
		regex_string = test
		regex_string = regex_string.replace("(","[");
		regex_string = regex_string.replace(")","]");
		regex_string = "^" + regex_string + "$"
		group_finder = re.compile(regex_string)
		for alien_word in alien_words:
			if not group_finder.search(alien_word)==None:
				num_matches += 1
		result = "Case #" + str(testIndex) + ": " + str(num_matches)
		print result