import sys

sDict = {
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
	'z': 'q'
}

def translate(c):
	
	if ord(c) >= ord('a') and ord(c) <= ord('z'):
		return sDict[c]
	
	return c

for i, line in enumerate(open(sys.argv[1]).readlines()[1:]):
	print "Case #%i: %s" % (i+1, ''.join(map(translate, line)).strip())
