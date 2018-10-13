zz= {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q', ' ': ' '}

f=open("input").readlines()
output=open("output","w+")
for x in range(1, int(f[0].strip())+1):
	output.write("Case #"+str(x)+": ")
	sentence = f[x].strip()
	for letter in sentence:
		output.write(zz[letter])
	output.write(chr(10))
print "done"
		
		
	


