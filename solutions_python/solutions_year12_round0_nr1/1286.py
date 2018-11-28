def remap(line):
	retval = ""
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
	for ch in line:
		if ch in d:
			retval += str(d[ch])
		else:
			retval += ch
	return retval


def main():
	t = input()

	i = 0
	while (i != t):
		line = raw_input()
		out = remap(line)
		print "Case #" + str(i+1) + ": " + out
		i += 1

if __name__ == '__main__':
	main()
