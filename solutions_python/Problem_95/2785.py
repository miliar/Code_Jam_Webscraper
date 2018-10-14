mapp = {' ': ' ', 'a': 'y', 'b': 'h', 'c': 'e', 'd': 's', 'e': 'o', 'f': 'c', 'g': 'v', 'h': 'x', 'i': 'd', 'j': 'u', 'k': 'i', 'l': 'g', 'm': 'l', 'n': 'b', 'o': 'k', 'p': 'r', 'q': 'z', 'r': 't', 's': 'n', 't': 'w', 'u': 'j', 'v': 'p', 'w': 'f', 'x': 'm', 'y': 'a', 'z': 'q'}

fin = open("A-small-attempt1.in",'r')
fout = open("out",'w') 

for i in range(int(fin.readline())):
	s = fin.readline()
	ans = "Case #"+repr(i+1)+": " 
	for j in range(0,len(s)-1):
		ans = ans+mapp[s[j]]
	fout.write(ans+'\n')
fout.close()		
	







