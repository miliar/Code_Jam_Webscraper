from string import Template
mapping = { 'a': 'y', 'b': 'h', 'c': 'e', 'd': 's', 'e': 'o', 'f': 'c', 'g': 'v', 'h': 'x', 'i': 'd', 'j': 'u', 'k': 'i', 'l': 'g', 'm': 'l', 'n': 'b', 'o': 'k', 'p': 'r', 'q': 'z', 'r': 't', 's': 'n', 't': 'w', 'u': 'j', 'v': 'p', 'w': 'f', 'x': 'm', 'y': 'a', 'z': 'q'}
def translate(s):
	retString = ''
	for x in range(len(s)):
		if s[x] == ' ':
			retString = retString + ' '
		elif s[x] == '\n':
			retString = retString
		else:
			retString = retString + mapping[s[x]]
	return retString
f = open('A-small-attempt1.in')
numLines = int(f.readline())
for x in range(numLines):
	print 'Case #' + str(x + 1) + ': ' + translate(f.readline())
