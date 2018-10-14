#!/usr/bin/python

def inp():
	fin=file("inp.txt", "r")
	fout=file("out.txt","a")
	test=fin.readline()
	for count in range(int(test)):
		case=fin.readline()
		result=compute(case)		
		out(result, count, fout)

def compute(case):
	case=case.split(" ")
	comb=case.pop(0)
	comblist=[]
	opplist=[]
	for move in range(int(comb)):
		comblist.append(case.pop(0))
	opp=case.pop(0)
	for oppose in range(int(opp)):
		opplist.append(case.pop(0))
	check=case.pop(0)
	teststr=case.pop(0)
	browse=1
	while browse<len(teststr):
		tmp=teststr[:browse]
		elem=teststr[browse]
		combo=checkComb(elem, tmp[-1], comblist)
		browse=browse+1
		if combo!=" ":
			teststr=tmp[:-1]+combo+teststr[browse:]
			browse=browse-1
		else:
			if checkOpp(elem, tmp, opplist)=="true":
				teststr=teststr[browse:]
				browse=1
	result="["
	if teststr=='\n':
		result="[]"
		return result
	for i in range(len(teststr)-1):
		result=result+teststr[i]+", "
	result=result[:-2]+"]"
	return result

def checkComb(elem1, elem2, comblist):
	combo=" "
	if(isBase(elem1)=="false" or isBase(elem2)=="false"):
		return combo
	for move in comblist:
		tmp=move[:2]
		if tmp.find(elem1)!=-1 and tmp.find(elem2)!=-1:
			if tmp.find(elem1)!=tmp.rfind(elem2):
				combo=move[2]
				return combo
	return combo
	

def checkOpp(elem, line, opplist):
	opp="false"
	if isBase(elem)=="false":
		return opp
	for move in opplist:
		if move.find(elem)!=-1:
			oppelem=str(move.replace(elem,""))
			if line.find(oppelem)!=-1:
				opp="true"
				return opp
	return opp

def isBase(elem):
	base="QWERASDF"
	if base.find(elem)==-1:
		return "false"
	return "true"

def out(result, count, fout):
	fout.write("Case #" + str(count+1) + ": " + str(result) + '\n')

def main():
	inp()

main()


