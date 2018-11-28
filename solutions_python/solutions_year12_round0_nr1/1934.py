

fin = open('A-small-attempt0.in', 'r')
fout = open('a.out', 'w')

cases = int(fin.readline().strip())

trans = {
	' ': ' ',
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
	'z': 'q',
}


for i in range(cases):
	line = fin.readline().strip()

	fout.write("Case #%d: " % (i + 1))

	for char in line:
		fout.write(trans[char])
	
	fout.write('\n')

fin.close()
fout.close()

	
