#m={}
#for _ in xrange(3):
#	a = raw_input()
#	b = raw_input()
#	for i in xrange(len(a)):
#		m[a[i]] = b[i]
#print m

m = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z' : 'q', 'q' : 'z'}


for i in xrange(int(raw_input())):
	a  = raw_input()
	s = []
	for j in a:
		s.append(m[j])
	s = ''.join(s)
	print "Case #%d: %s" % (i+1, s)
