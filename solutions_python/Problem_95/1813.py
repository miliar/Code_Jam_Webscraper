import sys
tr={' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm','q':'z','z':'q'}

with open(sys.argv[1],'r') as f:
	t=f.readline();
	t=int(t.strip());
	for i in range(0,t):
		g=f.readline().strip();
		e=''
		for j in range(0,len(g)):
			e=e+tr[g[j]];
		print "Case #%d: %s"%(i+1,e)


