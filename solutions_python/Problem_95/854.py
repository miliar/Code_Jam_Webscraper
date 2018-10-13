#! /usr/bin/env python

tr = {
	'y': 'a',
	'f': 'c',
	'n': 'b',
	'c': 'e',
	'i': 'd',
	'l': 'g',
	'w': 'f',
	'k': 'i',
	'b': 'h',
	'o': 'k',
	'u': 'j',
	'x': 'm',
	'm': 'l',
	'e': 'o',
	's': 'n',
	'z': 'q',
	'v': 'p',
	'd': 's',
	'p': 'r',
	'j': 'u',
	'r': 't',
	't': 'w',
	'g': 'v',
	'a': 'y',
	'h': 'x',
	'q': 'z',
}

def main(args):
	with open(args[1]) as inp:
		cases = int(inp.readline())
		for i in range(cases):
			line = inp.readline().strip()
			newline = ""
			for x in line:
				if x in tr:
					x = tr[x]
				newline += x
			print "Case #%d: %s" % (i+1, newline)

if __name__ == '__main__':
	import sys
	main(sys.argv)
