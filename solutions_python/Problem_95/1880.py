
lang = { 'e':'o', 'j': 'u', 'p':'r','m':'l','y':'a', 's':'n','l':'g'}
lang['c'] = 'e'
lang['d'] = 's'
lang['k'] = 'i'
lang['x'] = 'm'
lang['v'] = 'p'
lang['n'] = 'b'
lang['r'] = 't'
lang['i'] = 'd'
lang['b'] = 'h'
lang['t'] = 'w'
lang['a'] = 'y'
lang['h'] = 'x'
lang['w'] = 'f'
lang['f'] = 'c'
lang['o'] = 'k'
lang['g'] = 'v'
lang['u'] = 'j'
lang['z'] = 'q'
lang['q'] = 'z'

def problemA(filename,outputFile):
	f = open(filename,"r")
	input = f.readlines()
	testCases = int(input[0])
	output = ""
	for i, line in enumerate(input[1:]):
		output += "Case #" + str(i+1) + ": " + translate(line) 
	print(output)
	g = open(outputFile,"w")
	g.write(output)
	g.close()
	f.close()

def translate(line):
	s = ""
	for letter in line:
		try:
			lang[letter]
			s += lang[letter]
		except KeyError:
			s += letter;
	return s

problemA("input.txt","p1.txt")

