#!/usr/bin/env python

import sys

#Input
#3
#ejp mysljylc kd kxveddknmc re jsicpdrysi
#rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
#de kr kd eoya kw aej tysr re ujdr lkgc jv


#Output
#Case #1: our language is impossible to understand
#Case #2: there are twenty six factorial possibilities
#Case #3: so it is okay if you want to just give up

dec = {'a':'y', 
	'b':'h',
	'c':'e',
	'd':'s',
	'e':'o',
	'f':'c',
	'g':'v',
	'h':'x',
	'i':'d',
	'j':'u',
	'k':'i',
	'l':'g',
	'm':'l',
	'n':'b',
	'o':'k',
	'p':'r',
	'q':'z',
	'r':'t',
	's':'n',
	't':'w',
	'u':'j',
	'v':'p',
	'w':'f',
	'x':'m',
	'y':'a',
	'z':'q',
	' ':' '}


cases = int(sys.stdin.readline())

for i in range(1,cases+1):
	inp = sys.stdin.readline()
	out = ''
	for c in inp:
		if(c in dec):
			out += dec[c]
	print('Case #{}: {}'.format(i, out))