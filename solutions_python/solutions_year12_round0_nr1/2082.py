dict={
	'q':'z',
	'e':'o',
	'j':'u',
	'p':'r',
	'm':'l',
	'y':'a',
	's':'n',
	'l':'g',
	'c':'e',
	'k':'i',
	'd':'s',
	'x':'m',
	'v':'p',
	'i':'d',
	'g':'v',
	'a':'y',
	'r':'t',
	'o':'k',
	'n':'b',
	'b':'h',
	't':'w',
	'h':'x',
	'w':'f',
	'f':'c',
	'u':'j',
	'z':'q',
	' ':' '
}

def dictR(char):
	return dict[char]

numLines=int(raw_input())
for i in xrange(1,numLines+1):
	string=raw_input()
	print 'Case #%d: %s'%(i,''.join(map(dictR,string)))
