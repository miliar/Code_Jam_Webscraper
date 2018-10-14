import sys

dMap = {'a': 'y',
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


infile = sys.argv[1]
oF = open(infile,'r')

n = int(oF.readline())

for i in range(n):
	sen = oF.readline().strip().split()
	news = []
	for word in sen:
		w = ''
		for ch in word:
			w = w+dMap[ch]
		news.append(w)
	s = ' '.join(news)
	print 'Case #%d: %s'%(i+1,s)


