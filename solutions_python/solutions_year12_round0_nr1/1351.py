filename = 'file.in'


mapping =  {
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
	'z':'q',
	'\n':'',
	' ': ' '}


with open(filename, 'r') as inputfile:
	rows = int(inputfile.readline())
	for i in range(rows):
		line = inputfile.readline()
		chars = list(line)
		outputline = ""
		for char in chars:
			outputline += mapping[char]
		print "Case #" + str(i+1) + ": " + outputline

