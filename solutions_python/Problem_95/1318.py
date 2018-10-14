import sys
import string


def missingLetters(lis):
	result = []
	for c in string.ascii_lowercase:
		if not c in lis:
			result.append(c)
	
	return result 

trainInput = ["ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv",
"y qee"]


trainOuput = ["our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up",
"a zoo"]



trans = {} # Alien to English...

print "Training"
for i in range(len(trainInput)):
	linea = trainInput[i]
	lineb = trainOuput[i]
	
	for j in range(len(linea)):
		ca = linea[j]
		cb = lineb[j]
		
		if not ca in trans.keys():
			trans[ca] = cb
		else:
			if trans[ca] != cb:
				print ":("
				print "ca", ca , cb, i 
				sys.exit(-1)

print "Trained", len(trans.keys()), "should be 27"
print "missing googleian", missingLetters(trans.keys())
print "missing english", missingLetters(trans.values())

trans [ missingLetters( trans.keys() ) [0] ] = missingLetters( trans.values() )[0]
print "Trained", len(trans.keys()), "should be 27"
print "missing googleian", missingLetters(trans.keys())
print "missing english", missingLetters(trans.values())

EnglishToAlien = {}

for alien in trans.keys():
	EnglishToAlien[trans[alien]] = alien


print "testing"
f = file(sys.argv[1], "r")
fo = file(sys.argv[2], "w")

#fo.write("Output\r\n")
i = 1

for line in f:
	line = line.strip()
	if line == "Input":
		continue
	try:
		int(line)
		continue
	except:
		pass
		
	caseout = ""
	for c in line:
		caseout += trans[c]
	
	fo.write("Case #"+str(i)+": "+caseout+"\r\n")
	i += 1

fo.close()
f.close()
	
			
	

