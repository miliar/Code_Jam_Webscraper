import re

gd = {}
replacer = re.compile(r"[a-z ]")

def generateTranslationDict():
	de = zip("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand")
	for k,v in de:
		gd[k]=v
	de = zip("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities")
	for k,v in de:
		gd[k]=v
	de = zip("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up")
	for k,v in de:
		gd[k]=v
	gd['y']='a'
	gd['e']='o'
	gd['q']='z'
	alphabet = set([chr(c) for c in range(ord('a'), ord('z')+1)])
	gd[list(alphabet - set(gd.keys()))[0]] = list(alphabet - set(gd.values()))[0]

def readAndProcessInput(file_name, output_file_name=None):
	input_file = open(file_name, "r")
	if not output_file_name:
		output_file = open(file_name+".out", "w")
	else:
		output_file = open(output_file_name, "w")
	sNumCases = re.search(r"[\d]+", input_file.readline())
	if sNumCases:
		num_cases = int(sNumCases.group())
	for i in range(num_cases):
		l = input_file.readline()
		if l:
			translation = replacer.sub(lambda x: gd[x.group()], l)
			output_file.write("Case #X: S".replace("X", str(i+1)).replace("S", translation))
	output_file.close()
	input_file.close()

generateTranslationDict()
