the_map = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', ' ':' ', 'z': 'q', 'q': 'z'}

def problem():
	cases = int(raw_input())
	
	for i in xrange(cases):
		case(i + 1)

def case(i):
	line = raw_input()
	trans = ''
	
	for c in line:
		trans += the_map[c]
	
	print 'Case #%d:' % i, trans

if __name__ == '__main__':
	problem()
