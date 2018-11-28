import string

trans = {' ': ' ',
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

trans_table = string.maketrans(
	string.join(trans.keys(), ''),
	string.join(trans.values(), ''))

N = input()

for n in range(N):
	line = raw_input()
	print "Case #%d: %s" % (n + 1, line.translate(trans_table).strip())
