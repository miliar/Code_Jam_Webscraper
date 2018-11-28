import sys
import string

mapping = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

def translate(s):
	res = ''
	for a in s:
		if a in mapping:
			res += mapping[a]
		elif a != '\n':
			res += a	
	return res	


f = open("test.out", 'w')
cases = open("test.in", 'r').readlines()
T = int(cases[0])
i = 0
for i in xrange(T):
	c = cases[i+1]
	result = translate(c)
	line = "Case #" + str(i+1) + ": " + str(result)
	i = i + 1
	print line
	f.write(line + "\n")
f.close()