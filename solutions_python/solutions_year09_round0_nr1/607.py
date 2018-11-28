file_name = 'A-large'
input = open(file_name + '.in', 'r')
#input = open('alien_lang_example.in', 'r')
first_line = input.readline()
(chars_per_word, number_of_words, number_of_test_cases) = first_line.split()
print ('%s %s %s' % (chars_per_word, number_of_words, number_of_test_cases))
words = []
test_cases = []
for i in range(0, int(number_of_words)):
	words.append(input.readline().strip())
print words
for i in range(0, int(number_of_test_cases)):
	test_cases.append(input.readline().strip())
print test_cases

def convert_to_regex_pattern(t):
	regex_pattern = ''
	flag = False
	for c in t:
		if flag and regex_pattern[-1] != '(' and regex_pattern[-1] != ')':
			regex_pattern = regex_pattern + '|'
		if c == '(':
			flag = True
		if c == ')':
			flag = False
			regex_pattern = regex_pattern.rstrip('|')
		regex_pattern = regex_pattern + c
	return regex_pattern
import re
def solve(t):
	count = 0
	
	pattern = re.compile(convert_to_regex_pattern(t))
	#print convert_to_regex_pattern(t)
	for w in words:
		if pattern.match(w):
			count+=1
	return count
output = open(file_name + '.out', 'w')
for i,t in enumerate(test_cases):
	s = 'Case #%d: %d\n' % (i+1, solve(t))
	print s
	output.write(s)
input.close()
output.close()



