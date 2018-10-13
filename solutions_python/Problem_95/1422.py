import sys

#entrada = sys.argv[1]


D = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm','q':'z','z':'q'}

def DD(x):
	if x in D:
		return D[x]
	return x

fin = open('A-small-attempt6.in',"r")

N = int(fin.readline().strip())

for i in xrange(1,N+1):
	linea = str(fin.readline().strip())
	print 'Case #' +str(i) + ': ' + ''.join(DD(x) for x in linea)
