case1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
case2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
case3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv"

case1en = "our language is impossible to understand"
case2en = "there are twenty six factorial possibilities"
case3en = "so it is okay if you want to just give up"

# print # list(case1)

translateDict = {"a":"y", "o":"e", "z":"q", "\n":"\n", "q":"z"}


cases = [case1, case2, case3]
for case in cases:
	caseList = list(case)
	
	if case == case1:
		caseListEn = list(case1en)
	elif case == case2:
		caseListEn = list(case2en)
	else:
		caseListEn = list(case3en)
		
	for i in range(len(caseList)):
		if ~(list(caseList[i]) in translateDict.keys()):
			translateDict[caseList[i]] = caseListEn[i]


f = open("A-small-attempt1.in")

fout = open("outfile.out", "w")
num = int(f.readline())
n = 1
for line in f:
	
	newLine = []
	for c in list(line):
		newLine.append(translateDict[c])

	fout.write("Case #" + str(n) + ": " + "".join(newLine))
	n = n+1
fout.close()
f.close()