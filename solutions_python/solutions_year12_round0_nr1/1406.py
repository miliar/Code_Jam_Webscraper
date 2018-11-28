
googlese = {
	'a':'y',
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
	'z':'q',
	'y':'a',
	' ':' ',
	'\n':'',
	'\r':''
}

def convert(s):
	r = ''
	for i in s:
		r = r + googlese[i]
	return r

def output(c,s):
	print 'Case #'+str(c)+': '+convert(s)
	
def handle_input(inp):
	c = 1
	for l in inp[1:]:
		output(c,l)
		c=c+1
		
fd = file('input.in')
handle_input(fd.readlines())
fd.close()

