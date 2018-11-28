

m = dict(z='q', q='z')

import string
import sys


if __name__=='__main__':
	inp = open('input.txt', 'r').readlines()[1:]
	out = open('output.txt', 'r').readlines()
	for i in xrange(3):
		for j in enumerate(inp[i]):
			print j
			m[j[1]] = out[i][j[0]]
	for i in string.lowercase:
		print i,m.get(i)

	n = int(sys.stdin.readline())
	rez = open('rez.txt', 'w')
	for i in xrange(n):
		inp = sys.stdin.readline()
		out_line = ''.join(map(lambda x: m[x], inp))
		rez.write('Case #%d: %s' % (i+1, out_line))
		print out_line
		



