translate = {
	'a': 'y',
	'b': 'h',
	'c': 'e',
	'd': 's',
	'e': 'o',
	'f': 'c',
	'g': 'v',
	'h': 'x',
	'i': 'd',
	'j': 'u',
	'k': 'i',
	'l': 'g',
	'm': 'l',
	'n': 'b',
	'o': 'k',
	'p': 'r',
	'q': 'z',
	'r': 't',
	's': 'n',
	't': 'w',
	'u': 'j',
	'v': 'p',
	'w': 'f',
	'x': 'm',
	'y': 'a',
	'z': 'q'}

gFile = open('googlerese.in', 'r')
outFile = open('outputFile.out', 'w')
outputCount = gFile.readline()
newCount = int(outputCount)
if newCount > 30:
	newCount = 30
j=1
i=0

while j <= newCount:
	outFile.write('Case #' + str(j) + ': ')
	transline = gFile.readline()
	for i in range(len(transline)):
		if transline[i] != " ":
			if transline[i] == "\n":
				break
			outFile.write(translate[transline[i]])
		else:
			outFile.write(' ')
	outFile.write('\n')
	j=j+1






gFile.close()
outFile.close()
