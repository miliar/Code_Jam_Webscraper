import re, urllib, string


DEBUG = 1

f=open("input","r")
lines = f.readlines()
f.close()

CHAR = [" ","a","c","d","e","j","l","m","o","t","w"];


def countOccurrances(text, pattern):
	tally = 0
	if (len(pattern)==1):
		tally = string.count(text, pattern)
	else:
		head = pattern[0]
		tail = pattern[1:]
		for i in range(0,len(text)):
			if (text[i] == head):
				tally = tally + countOccurrances(text[i+1:], tail)
	return tally

testcases = []
N = string.strip(lines[0]);
for i in range(1,int(N)+1):
	testcase = "";
	for each in list(string.strip(lines[i])):
		if (CHAR.__contains__(each)):
			testcase = testcase + each
	testcases.append(testcase);

if DEBUG: print testcases;

f=open("output","w")
ntestCase = 0
for eachCase in testcases:
	ntestCase = ntestCase + 1;
	nCount = countOccurrances(eachCase,"welcome to code jam")
	if (nCount < 9999):
		nCount = str(nCount).rjust(4, '0')
	if (DEBUG): print "Case #%s: %s %s\n" % (ntestCase, str(nCount)[-4:], eachCase)
	f.write("Case #%s: %s\n" % (ntestCase, str(nCount)[-4:]))

f.close()