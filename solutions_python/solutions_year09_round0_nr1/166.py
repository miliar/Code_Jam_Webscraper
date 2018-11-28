import re

def case2re(case):
	case = case.replace('(', '[')
	case = case.replace(')', ']{1}')
	return '^' + case + '$'

def parse(file):
	lines = open(file).readlines()
	lines = [line.strip() for line in lines]
	length, words, cases = [int(x) for x in lines[0].split(' ')]
	
	words_list = [w[:length] for w in lines[1:words+1]]
	cases_list = [re.compile(case2re(c)) for c in lines[words+1:]]
	
	for i, case in enumerate(cases_list):
		l = len([1 for w in words_list if case.match(w)])
		print('Case #%s: %s' % (i+1, l))
	
parse('A-large.in')