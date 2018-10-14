import sys


def buildDict():
	d = dict({})
	alpha = 'abcdefghijklmnopqrstuvwxyz '
	for a in alpha:
	  d[a] = 0
	d['z'] = 'q'
	d['q'] = 'z'

	cipher = ['ejp mysljylc kd kxveddknmc re jsicpdrysi', 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'de kr kd eoya kw aej tysr re ujdr lkgc jv']
	key = ['our language is impossible to understand', 'there are twenty six factorial possibilities', 'so it is okay if you want to just give up']
	for i in range(0,len(cipher)):
		for c in range(0,len(cipher[i])):
			d[cipher[i][c]] = key[i][c]

	return d
	
def translate(line, d):
	s = ''
	for c in line:
		s += d[c]

	return s
		

def main():

	fIn = sys.argv[1]

	d = buildDict()

	with open(fIn, 'r') as f:
		garbage = f.readline() # Throw away the first line
		i = 0
		for line in f:
			i = i+1
			print 'Case #%d: '%i + translate(line.strip(), d)

if __name__ == '__main__':
	sys.exit(main())
