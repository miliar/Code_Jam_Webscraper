def final():
	encoding={' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
	jrt=input("filename")
	inp=open(jrt,"r")
	out=open("decoded.txt","w")
	first=inp.readline()
	first=first.strip()
	first=int(first)
	for k in range(0,first):
		s=inp.readline().strip()
		h=""
		for i in range(0,len(s)):
			h=h+encoding[s[i]]
		out.write("Case #"+str(k+1)+":"+" "+h+"\n")
	out.close()
	inp.close()
final()