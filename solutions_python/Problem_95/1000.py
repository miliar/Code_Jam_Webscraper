import sys

if __name__ == "__main__":
	nb = int(sys.stdin.readline())
	cpt = 1
	
	d = {}
	d['a'] = 'y'
	d['b'] = 'h'
	d['c'] = 'e'
	d['d'] = 's'
	d['e'] = 'o'	
	d['f'] = 'c'
	d['g'] = 'v'
	d['h'] = 'x'
	d['i'] = 'd'
	d['j'] = 'u'
	d['k'] = 'i'
	d['l'] = 'g'
	d['m'] = 'l'
	d['n'] = 'b'
	d['o'] = 'k'
	d['p'] = 'r'
	d['q'] = 'z'
	d['r'] = 't'
	d['s'] = 'n'
	d['t'] = 'w'
	d['u'] = 'j'
	d['v'] = 'p'
	d['w'] = 'f'
	d['x'] = 'm'
	d['y'] = 'a'
	d['z'] = 'q'
	d[' '] = ' '
	
	while cpt <= nb:
		line = sys.stdin.readline()
		newline = ''
		string = 'Case #'+str(cpt)+':'
		for i in range(len(line)):
			if line[i] != '\n':
				newline += d[line[i]]

		string = string+' '+newline
		print string
		cpt += 1