import sys 


if len(sys.argv) > 1 and sys.argv[1]: 
	f = open(sys.argv[1])
	a = f.read()
	f.close()
else:
	a = '''3
	ejp mysljylc kd kxveddknmc re jsicpdrysi
	rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
	de kr kd eoya kw aej tysr re ujdr lkgc jv'''

c = a.split('\n')

def check(s):
	str = ''
	p = {
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
		'z':'q', # not yet
		'p':'r',
		'd':'s',
		'r':'t',
		'j':'u',
		'g':'v',
		't':'w',
		'h':'x',
		'a':'y',
		'q':'z', # not yet
		' ':' ',
		'\t':'\t'
		}
	for i in s:
		str += p[i]
	return str

if len(sys.argv) > 2 and sys.argv[2]:
	w = file(sys.argv[2], 'w')
else:
	w = file('A-small-0.out', 'w')

for i in range(int(c[0])):

	#result = check(c[i+1])
	w.write('Case #%d: %s\n' % (i+1, check(c[i+1])))
	#print 'Case #%d: %s\n' % (i+1, result)

w.close()

