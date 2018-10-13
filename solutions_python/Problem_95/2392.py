# speaking in tongues

# here are our letter mappings for translation
mapDict = {'y': 'a', 'n':'b', 'f':'c', 'i':'d', 'c':'e', \
			'w':'f', 'l':'g', 'b':'h', 'k':'i', 'u':'j', \
			'o':'k', 'm':'l', 'x':'m', 's':'n', 'e':'o', \
			'v':'p', 'z':'q', 'p':'r', 'd':'s', 'r':'t', \
			'j':'u', 'g':'v', 't':'w', 'h':'x', 'a':'y', \
			'q':'z'} 
	
inFile = open("A-small-attempt1.in", "r")

numCases = int(inFile.readline())
x = 1

while x <= numCases:
	line = inFile.readline()
	line.strip()
	line.split(" ")

	newLine = ""
	for c in line:
		if c != " " and c != "\n":
			newLine = newLine + mapDict[c]
		else:
			newLine = newLine + " "

	print "Case #" + str(x) + ": " + newLine
	
	x = x + 1