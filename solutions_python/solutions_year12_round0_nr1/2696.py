from IO import readline,writeline



fileNameIn = 'A-small-attempt0.in' 
fileNameOut= 'test.out'

cipher = [('a','y'),('b','h'),('c','e'),('d','s'),('e','o'),('f','c'),('g','v'),('h','x'),('i','d'),('j','u'),('k','i'),('l','g'),('m','l'),('n','b'),('o','k'),('p','r'),('q','z'),('r','t'),('s','n'),('t','w'),('u','j'),('v','p'),('w','f'),('x','m'),('y','a'),('z','q')]


def find(x,cipher):
	for a in cipher:
		if a[0] == x:
			return a[1]
		


#print find('b',cipher)


def decrypt(string,cipher):
	output = []
	for c in string:
		if c == ' ':
			output.append(' ')
		else:
			output.append(find(c,cipher))
	return ''.join(output)
	#return output


n = int(readline(fileNameIn,0))
i = 1
output = []
while i < n+1:
	string = readline(fileNameIn,i)
	#print type(string)
	output.append("Case #" + str(i) + ": " + decrypt(string[:-1],cipher) + "\n")
	i = i + 1
#print output
writeline(fileNameOut,''.join(output))









#print decrypt("abcdefghijklmnopqrstuvwxyz",cipher)

#print decrypt("ejp mysljylc kd kxveddknmc re jsicpdrysi",cipher)

#print decrypt("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",cipher)
		
#print decrypt("de kr kd eoya kw aej tysr re ujdr lkgc jv",cipher)
