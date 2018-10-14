print("Start.")
lineNum = 1
inputFile = open('input')
expectedlineNum = int(inputFile.readline()[:-1])
print(expectedlineNum)
outputFile = open('output', 'w')
translate = {'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v', 'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b', 'o':'k', 'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j', 'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q', ' ':' ', '\n':''}
for line in (inputFile.readlines()):
	newLine=[]
	for x in line[:]:
			newLine.append(translate[x])
	print("Case #"+str(lineNum)+": "+"".join(newLine))
	if(lineNum<expectedlineNum):
		outputFile.write("Case #"+str(lineNum)+": "+"".join(newLine)+"\n")
		lineNum = lineNum + 1
	else:
		outputFile.write("Case #"+str(lineNum)+": "+"".join(newLine))
outputFile.close()