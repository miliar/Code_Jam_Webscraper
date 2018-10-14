#from __future__ import print_function
import sys

toEnglish = {'a' : 'y',
'b' : 'h',
'c' : 'e',
'd' : 's',
'e' : 'o',
'f' : 'c',
'g' : 'v',
'h' : 'x',
'i' : 'd',
'j' : 'u',
'k' : 'i',
'l' : 'g',
'm' : 'l',
'n' : 'b',
'o' : 'k',
'p' : 'r',
'q' : 'z',
'r' : 't',
's' : 'n',
't' : 'w',
'u' : 'j',
'v' : 'p',
'w' : 'f',
'x' : 'm',
'y' : 'a',
'z' : 'q'}

data = sys.stdin.readlines()

num_test = int(data[0])

for i in range(0, num_test):
	sys.stdout.write('Case #%d: ' % (i + 1))
	for ch in data[i + 1]:
		if(not ch.isspace()):
			sys.stdout.write(toEnglish[ch])
		else:
			sys.stdout.write(ch)