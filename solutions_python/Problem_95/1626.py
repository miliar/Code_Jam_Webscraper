h = {"q":"z", "z":"q"}

def learn(text, translated_text):
	for i in range(len(text)):
		h[text[i]] = translated_text[i]
		
learn("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand")
learn("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities")
learn("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up")

#v = []
#for c in range(ord('a'), ord('z')+1):
	#v.append(h[chr(c)])
#	print(chr(c), h[chr(c)])

#v.sort()
#print(v)	

def translate(text):
	s = ""
	for ch in text:
		s += h[ch]
	return s
	
fin = open("in.txt", "r")
fout = open("out.txt", "w")

n = int(fin.readline())
for i in range(n):
	text = fin.readline().rstrip()
	fout.write("Case #" + str(i+1) + ": " + translate(text) + "\n")