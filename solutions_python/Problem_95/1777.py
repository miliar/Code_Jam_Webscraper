#!/usr/bin/env python

dictio = {
'y':'a',
'n':'b',
'f':'c',
'i':'d',
'c':'e',
'w':'f',
'l':'g',
'b':'h',
'k':'i',
'u':'j',
'o':'k',
'm':'l',
'x':'m',
's':'n',
'e':'o',
'v':'p',
'z':'q',
'p':'r',
'd':'s',
'r':'t',
'j':'u',
'g':'v',
't':'w',
'h':'x',
'a':'y',
'q':'z',
' ':' '
}

count=1
T = int(raw_input())
while T:

	inp = raw_input()
	out = map(lambda a: dictio[a], inp)
	
	print 'Case #'+str(count)+': '+''.join(out)


	count+=1
	T-=1
