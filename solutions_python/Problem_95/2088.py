import sys

def fillMappings(gString, eString, dict):
	if len(gString) != len(eString):
		 raise NameError('Invalid mappings strings')
	for i in range(len(gString)):
		dict[gString[i]] = eString[i]

def createMappings():
	origGoogleStrings = ["ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv", "qz"]
	origEnglishStrings = ["our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up", "zq"]
	dict = {}
	for i in range(len(origGoogleStrings)):
		fillMappings(origGoogleStrings[i], origEnglishStrings[i], dict)
	return dict
	
def translateStr(srcStr, dict):
	res = ""
	for curChar in srcStr:
		res += dict[curChar];
	return res
#main

mappings = createMappings()
if len(mappings) != 26 + 1:
	raise NameError('Wrong mapping created')

	
	
if len(sys.argv) < 2:
     sys.exit("use argument; error")
input = open(sys.argv[1], "r")
output = open(sys.argv[1] + ".out", "w")

count = int(input.readline())

for curTestIndex in range(count):
	curInput = input.readline().strip()
	translatedInput = translateStr(curInput, mappings)
	output.write("Case #%d: %s\n" % (curTestIndex+1, translatedInput))

input.close()
output.close()    
print "success"
	



	
	
