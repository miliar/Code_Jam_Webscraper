from sys import *

def getEletter(gLetter):
	googlereseString = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'
	englishString = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'
	
	
	if gLetter == 'q':
		res = 'z'
	else:
		if gLetter == 'z':
			res = 'q'
		else:
			res = englishString[googlereseString.index(gLetter)]
	
	return res

def solve(_, line):
	
	enLine = ''
	for ch in line:
		enLine += getEletter(ch)
	
	print "Case #%d: %s" %(_+1, enLine)

# main code
cases = int(raw_input())
for _ in xrange(cases):
	line = raw_input()

	solve(_, line)
