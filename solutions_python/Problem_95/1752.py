if __name__=="__main__":
	iFile = open("G:/usaco/A-small-attempt1.in", 'r')
	oFile = open("G:/usaco/A-small-attempt1.out", 'w')
	num = (int)(iFile.readline())
	rules = {'q':'z', 'z':'q', ' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm'}
	for i in range(0, num):
		G = iFile.readline().strip('\n').strip('\r')
		G = "".join(G)
		N = "Case #"+str((i+1))+": "
		for j in range(0, len(G)):
			N = N+rules[G[j]]
		N = N+'\n'
		oFile.write(N)
		print(N)
	iFile.close()
	oFile.close()
