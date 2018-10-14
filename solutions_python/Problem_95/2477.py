lines = [line.strip() for line in open('input.in')]
alphabet = {
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
}

output = ""
i = 1

outputFile = open('output.txt', 'w')

for line in lines:
	output = ""
	if (i != 1):
		for c in line:
			try:
				output = output + alphabet[c]
			except:
				output = output + c
		print "Case #" + str(i-1) + ": " + output
		outputFile.write("Case #" + str(i-1) + ": " + output+"\n")
	i = i + 1

outputFile.close()