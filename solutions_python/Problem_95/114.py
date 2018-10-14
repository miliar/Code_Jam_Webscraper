


if __name__=='__main__':
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
	f = open('A-small-attempt1.in','r')
	f.readline()
	lines = [line for line in f]
	f.close()

	f1 = open('A.out','w')
	count = {}
	i = 1;
	
	for line in lines:
		line0 = line[:-1]
		tr = [d[c] for c in line0]	
		f1.write('Case #%d: '%(i))
		for c in tr:
			f1.write(c)
		f1.write('\n')
		i = i  + 1


	f1.close()
