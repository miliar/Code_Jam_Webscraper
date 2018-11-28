import sys


myDict = {}

samples = {"ejp mysljylc kd kxveddknmc re jsicpdrysi":"our language is impossible to understand",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd":"there are twenty six factorial possibilities",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv":"so it is okay if you want to just give up",
	"qz":"zq"}

# populating dict

for orig,trans in samples.iteritems():
	for i in range(0,len(orig)):
		if orig[i] != ' ':
			myDict[orig[i]] = trans[i]

# for orig,trans in myDict.iteritems():
# 	print orig,trans

def translate(orig):
	result = ""
	for i in range(0,len(orig)-1):
		if orig[i] != ' ':
			result += myDict[orig[i]]
		else:
			result += ' '
	return result

number = int(sys.stdin.readline())
myReturn = ""

for i in range(0,number):
	myReturn += "Case #"+str(i+1)+": "+translate(sys.stdin.readline())+"\n"

print myReturn