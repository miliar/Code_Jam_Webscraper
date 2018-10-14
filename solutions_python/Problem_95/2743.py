tl = {' ':' '}
tl['a'] = 'y'
tl['b'] = 'h'
tl['c'] = 'e'
tl['d'] = 's'
tl['e'] = 'o'
tl['f'] = 'c'
tl['g'] = 'v'
tl['h'] = 'x'
tl['i'] = 'd'
tl['j'] = 'u'
tl['k'] = 'i'
tl['l'] = 'g'
tl['m'] = 'l'
tl['n'] = 'b'
tl['o'] = 'k'
tl['p'] = 'r'
tl['q'] = 'z'
tl['r'] = 't'
tl['s'] = 'n'
tl['t'] = 'w'
tl['u'] = 'j'
tl['v'] = 'p'
tl['w'] = 'f'
tl['x'] = 'm'
tl['y'] = 'a'
tl['z'] = 'q'

f = open("a.in", 'r')

cases = int(f.readline())

line = ''

for cases in range(0,cases):
	line = f.readline()
	line = line.rstrip('\r\n')
	
	line = list(line)

	for i in range(len(line)):
		
		old = line[i]
		line[i] = tl[old]
	line = ''.join(line)

	print("Case #" + str(cases+1) + ": " + line)
