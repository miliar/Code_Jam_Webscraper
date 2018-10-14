import re, urllib, string
DEBUG = 0

f=open("input","r")
lines = f.readlines()
f.close()

wordlist = []
testcases = []
(L, D, N) = string.split(string.strip(lines[0])," ");
casenum=0
for i in range(1,int(D)+1):
	if DEBUG: print i, len(lines)
	wordlist.append(string.strip(lines[i]));

for i in range(int(D)+1,int(D)+int(N)+1):
	if DEBUG: print i, len(lines), L, D, N
	testcases.append(string.strip(lines[i]));

if DEBUG: print wordlist;
if DEBUG: print testcases;

f=open("output","w")
ntestCase = 0
for eachCase in testcases:
	ntestCase = ntestCase + 1;
	nCount = 0;
	eachCase = string.replace(eachCase, "(", "[");
	eachCase = string.replace(eachCase, ")", "]+");
	if DEBUG: print eachCase
	for eachword in wordlist:
		matches = re.findall(eachCase, eachword)
		nCount = nCount + len(matches)
	f.write("Case #%s: %s\n" % (ntestCase, nCount))

f.close()
