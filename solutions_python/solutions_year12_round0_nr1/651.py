def compute():
	dic = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'};
	f = open('A-small-attempt0.in');
	lines = f.readlines()
	numInputs = int(lines[0])
	for i in range(1, 1+numInputs):
		cLine = lines[i];
		originalLine = '';
		for j in range(0, len(cLine)-1):
			originalLine = originalLine + dic[cLine[j]];
		print "Case #"+str(i)+": "+originalLine


compute();
	
