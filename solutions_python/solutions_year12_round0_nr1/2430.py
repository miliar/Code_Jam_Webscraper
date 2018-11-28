fin = open('A-small-attempt1.in', 'r')
fout = open('3lines.out', 'w')
N = int(fin.readline())
x = {
	'e':'o', 'j':'u', 'p':'r', 'm':'l', 'y':'a', 's':'n', 'l':'g', 'c':'e', 'k':'i', 'd':'s', 'x':'m', 'v':'p', 'n':'b', 'r':'t', 
	'i':'d', 'b':'h', 't':'w', 'a':'y', 'h':'x', 'w':'f', 'f':'c', 'u':'j', 'q':'z', 'g':'v', 'o':'k', 'z':'q', ' ':' '}


for i in range(N):
	y = fin.readline()
	newStr = ''
	for j in range(len(y)):
		if y[j] in x:
			newStr += x[y[j]]
	fout.write('Case #' + str(i + 1) + ': ' + newStr + '\n')

