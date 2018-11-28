def translate(line, dictionary):
	translatedLine = ""
	for c in line:
		if c in dictionary:
			translatedLine += dictionary[c]
		else:
			translatedLine += c
	return translatedLine

dictionary = {  'a':'y',
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
		}

f = open('A-small-attempt1.in', 'r')
fwrite = open('A-small-attempt1.out', 'w')
f.readline()
i = 0
for line in f:
	i = i + 1
	fwrite.write("Case #" + str(i) + ": " + translate(line, dictionary))
