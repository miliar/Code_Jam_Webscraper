import os

googlerese = {'a':'y','b':'h','c':'e','d':'s','e':'o',
	      'f':'c','g':'v','h':'x','i':'d','j':'u',
	      'k':'i','l':'g','m':'l','n':'b','o':'k',
              'p':'r','q':'z','r':'t','s':'n','t':'w',
	      'u':'j','v':'p','w':'f','x':'m','y':'a','z':'q',' ':' '}

def readFile(afile):
	myfile = open(afile)
	return [line.strip('\n') for line in myfile.readlines()]

def translate(lines):
	lines = lines[1:]
	translate = []
	num = 1
	for case in lines:
		newline = "Case #" + str(num) + ": "
		for char in case:
			newline += googlerese[char]
		translate.append(newline)
		num += 1
	return(translate)

def writeFile(text):
	output = file("output.txt", "w")

	for line in text:
		output.write("%s\n" % line)
writeFile(translate(readFile("A-small-attempt0.txt")))
