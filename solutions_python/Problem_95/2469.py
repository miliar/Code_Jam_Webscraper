from string import atoi
mapping = {
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
		' ':' ',
		}
fin = file('A-small-attempt0.in', 'r')
case = 1
for f in range(atoi(fin.readline().strip())):
	line = fin.readline().strip()
	lout = ''	
	for c in line:
		lout += mapping[c]
		
	print 'Case #%d: %s'%(case, lout)
	case += 1

