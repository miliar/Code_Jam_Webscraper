from string import maketrans

mapping = {	'a':'y',
				'b':'n',
				'c':'f',
				'd':'i',
				'e':'c',
				'f':'w',
				'g':'l',
				'h':'b',
				'i':'k',
				'j':'u',
				'k':'o',
				'l':'m',
				'm':'x',
				'n':'s',
				'o':'e',
				'p':'v',
				'q':'z',
				'r':'p',
				's':'d',
				't':'r',
				'u':'j',
				'v':'g',
				'w':'t',
				'x':'h',
				'y':'a',
				'z':'q' }

intab,outtab = '',''	
for key, val in mapping.items():
	intab += val
	outtab += key

trantab = maketrans(intab, outtab)
T = raw_input()
out,i='',1
for k in range(int(T)):
	mystr = raw_input()
	out += 'Case #' + str(i) + ': ' + mystr.translate(trantab)
	if i<T: out += '\n'
	i = i+1
	
print(out)