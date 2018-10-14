import sys

def translate_letter(letter):
	mapper = {'y':'a', 'n':'b', 'f':'c', 'i':'d',
			'c':'e', 'w':'f', 'l':'g', 'b':'h', 'k':'i',
			'u':'j', 'o':'k', 'm':'l', 'x':'m', 's':'n',
			'e':'o', 'v':'p', 'z':'q', 'p':'r', 'd':'s',
			'r':'t', 'j':'u', 'g':'v', 't':'w', 'h':'x',
			'a':'y', 'q':'z'}
	return mapper[letter]

def translate(aWord):
	return ''.join(map(lambda x: translate_letter(x), aWord))

input_file = open(sys.argv[1], "r")
output_file = open(sys.argv[2], "w")

cases = int(input_file.next())

for i in range(cases):
	words = map(lambda x: x.strip(),input_file.next().split(" "))
	result = ' '.join(map(translate, words))
	output_file.write("Case #{0}: {1}\n".format(i+1, result))

input_file.close()
output_file.close()