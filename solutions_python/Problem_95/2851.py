entrada = open('A-small-attempt0.in', 'r')
saida = open('A-small-attempt0.out', 'w')

tradutor = {'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v', 'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l',
					  'n':'b', 'o':'k', 'p':'r', 'q':'z','r':'t', 's':'n', 't':'w', 'u':'j', 'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q'}

num = 1

for linha in entrada.readlines()[1:]:
	saida.write('Case #' + str(num) + ': ')
	for c in linha:
		if(c != ' ' and c != '\n'):
			saida.write(tradutor[c])
		else:
			saida.write(c)
	num = num + 1
