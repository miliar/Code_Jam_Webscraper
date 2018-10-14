def	readint():
	return	(list(map(int,	sys.stdin.readline().strip().split(" "))))
def	readstr():
	return	(list(map(str,	sys.stdin.readline().strip().split(" "))))	
def	rline():
	return sys.stdin.readline().strip()
def	main():
	pass
	
if	__name__=='__main__':
	import	sys
	testcase =	int(rline())
	dict = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b',
 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z':'q','q':'z'}
	for i in range(testcase):
		s = str(rline())
		outstr = ''
		for c in s:
			if c != ' ':
				outstr += dict[c]
			else:
				outstr+= ' '
		print ('Case #%d: %s' % ((i+1), outstr))
	main()