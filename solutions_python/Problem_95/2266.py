
inp = file("myfile.in","r")
out = file('outputfile','w')

data = inp.read()

k = data.split('\n')



mydict = {
	'\n':'\n',
	' ':' ', 
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
	'y':'a',
	'z':'q'
	};


u = ''

for x in range(1,int(k[0])+1):
	for i in k[x]:
		u = u +mydict[i]
	v='Case #'+str(x)+': '+u
	out.write(v)
	out.write('\n')
	u=''

	
inp.close()
out.close()

