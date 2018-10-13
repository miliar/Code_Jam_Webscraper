mapping = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's',
 			'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i',
 			'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 
			'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j',
			't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm',
			 'z': 'q', ' ': ' '}

f = open('sample.txt', 'r')
fout = open('output.txt', 'w')
fContent = f.read().split('\n')
n = int(fContent[0])
for i in range(n):
	fout.write('Case #'+ str(i+1) + ': ' + ''.join([mapping[ch] for ch in fContent[i+1]]) + '\n')
f.close()
fout.close()