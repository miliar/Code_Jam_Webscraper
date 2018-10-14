letters = {
			'a': 'y',
			'o': 'k',
			'z': 'q',
			'e': 'o',
			'j': 'u',
			'p': 'r',
			'm': 'l',
			'y': 'a',
			's': 'n',
			'l': 'g',
			'c': 'e',
			'k': 'i',
			'd': 's',
			'x': 'm',
			'v': 'p',
			'n': 'b',
			'r': 't',
			'i': 'd',
			'b': 'h',
			't': 'w',
			'k': 'i',
			'h': 'x',
			'w': 'f',
			'f': 'c',
			'u': 'j',
			'g': 'v',
			'q': 'z'
			}
f = open('in')
g = open('out', 'w')
num = int(f.readline())

for i in xrange(1, num +1):
	_in = f.readline()
	_out = 'Case #%i: ' % i

	for x in xrange(len(_in)):
		if _in[x] in letters:
			_out += letters[_in[x]]
		else:
			_out += _in[x]

	g.write(_out)