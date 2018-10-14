gooToEng = {'y':'a', 'n':'b', 'f':'c', 'i':'d', 'c':'e', 'w':'f', 'l':'g', 'b':'h', 'k':'i', 'u':'j', 'o':'k', 'm':'l', 'x':'m', 's':'n', 'e':'o', 'v':'p', 'z':'q', 'p':'r', 'd':'s', 'r':'t', 'j':'u', 'g':'v', 't':'w', 'h':'x', 'a':'y', 'q':'z'}

f = open("A-small-attempt1.in", "r")
out = open("output", "w")
numInput = f.readline();
for i in range(0, int(numInput)):
	outputLine = ""
	input = f.readline()
	words = input.split()
	for w in words:
		for n in range(0, len(w)):
			outputLine += str(gooToEng.get(w[n]))
		outputLine += " "
	out.write('Case #'+str(i+1)+': '+outputLine+'\n')
f.close()
out.close()