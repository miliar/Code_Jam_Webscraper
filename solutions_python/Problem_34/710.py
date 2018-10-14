# A pattern is repped by a list of list
# Each sublist contains letters matched by it
# EX: - (ab)c = [['a', 'b'], ['c']]


def match_letter(letter, token):
	return letter in token

def match_pattern(string, pat):
	for letter, token in zip(string, pat):
		if not match_letter(letter, token):
			return False
	return True


def string_to_group(string):
	i = 1
	group = []
	while string[i] != ')':
		group.append(string[i])
		i = i + 1
	return (group, i) # Return group and index to skip past it

def string_to_pattern(string):
	i = 0
	pattern = []
	l = len(string)
	while i < l:
		if string[i] == '(': # A group
			g, j = string_to_group(string[i:])
			pattern.append(g)
			i = i + j + 1
		else: # A letter
			pattern.append([string[i]])
			i = i + 1
	return pattern


s = raw_input()
L, D, N = map(lambda a: int(a), s.split())


data = [] # This list contains all Data received from aliens
for s in range(D):
	data.append(raw_input())

case = 1
for p in range(N):
	pattern = string_to_pattern(raw_input()) # Scan a pattern
	matched = 0
	for d in data:
		if match_pattern(d, pattern): # Check it with all strings
			matched = matched + 1
	print "Case #%d: %d" %(case, matched)
	case = case + 1
