
def translate(m, t):
	result = ''
	for x in m:
		result = result + t[x]
	return result


def write_case(i, z, o):
	o.write('Case #' + str(i) + ': ' + str(z) + '\n')

t = {'a':'y',
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
	 ' ':' ',
	 '\n':''
	}


f = open('a_in_small.txt')
o = open('a_out_small.txt', 'w')
Count = int(f.readline())
i = 1

for l in f:
	g = translate(l, t)
	write_case(i, g, o)
	i += 1

o.close()
f.close()