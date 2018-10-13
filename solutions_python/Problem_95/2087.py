#!/usr/bin/python

def do_convert(string):
	news = ''
	for c in string:
		newc = ''
		if c == 'y':
			newc = 'a'
		elif c == 'n':
			newc = 'b'
		elif c == 'f':
			newc = 'c'
		elif c == 'i':
			newc = 'd'
		elif c == 'c':
			newc = 'e'
		elif c == 'w':
			newc = 'f'
		elif c == 'l':
			newc = 'g'
		elif c == 'b':
			newc = 'h'
		elif c == 'k':
			newc = 'i'
		elif c == 'u':
			newc = 'j'
		elif c == 'o':
			newc = 'k'
		elif c == 'm':
			newc = 'l'
		elif c == 'x':
			newc = 'm'
		elif c == 's':
			newc = 'n'
		elif c == 'e':
			newc = 'o'
		elif c == 'v':
			newc = 'p'
		elif c == 'z':
			newc = 'q'
		elif c == 'p':
			newc = 'r'
		elif c == 'd':
			newc = 's'
		elif c == 'r':
			newc = 't'
		elif c == 'j':
			newc = 'u'
		elif c == 'g':
			newc = 'v'
		elif c == 't':
			newc = 'w'
		elif c == 'h':
			newc = 'x'
		elif c == 'a':
			newc = 'y'
		elif c == 'q':
			newc = 'z'
		else:
			newc = c

		news += newc

	return news

f = open('A-small-attempt2.in', 'r')
n = int(f.readline())
for i in range(1, n+1):
	string = f.readline()
	string = string[0:len(string)-1]
	string = do_convert(string)
	print "Case #" + str(i) + ": " + string[0:len(string)]
