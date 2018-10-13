from sys import argv

dictionary = {'y' : 'a', 'n' : 'b', 'f' : 'c', 'i' : 'd', 'c' : 'e', 'w' : 'f', 'l' : 'g', 'b' : 'h', 'k' : 'i', 'u' : 'j', 'o' : 'k', 'm' : 'l', 'x' : 'm', 's' : 'n', 'e' : 'o', 'v' : 'p', 'z' : 'q', 'p' : 'r', 'd' : 's', 'r' : 't', 'j' : 'u', 'g' : 'v', 't' : 'w', 'h' : 'x', 'a' : 'y', 'q' : 'z'}

txt = open('A-small-attempt1.in')
n = int(txt.readline())

target = open('output.txt', 'w')

for i in range(n):
	line = txt.readline()
	result = ''
	for letter in line:
		if letter == ' ':
			result += ' '
		elif letter == '\n':
			result = result
		else:
			result += dictionary[letter]
	target.write('Case #%d: %s\n' % (i + 1, result))
