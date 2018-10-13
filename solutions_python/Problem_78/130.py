#!/usr/bin/python

def inp():
	fin=file('in.txt','r')
	fout=file('out.txt','a')
	testCases=fin.readline()
	for count in range(int(testCases)):
		case=fin.readline()
		result=compute(case)
		out(count,result,fout)

def compute(case):
	result="Broken"
	params=case.split(" ")
	limit=params.pop(0)
	perD=params.pop(0)
	perG=params.pop(0)
	if int(perG)==100:
		if int(perD)!=100:
			return result
	if int(perG)==0:
		if int(perD)!=0:
			return result
	itr=0
	while(result=="Broken" and itr<int(limit)):
		calc=(itr+1)*int(perD)
		mod=calc%100
		if mod==0:
			result="Possible"
		itr=itr+1
	return result

def out(count,result,fout):
	fout.write("Case #" + str(count+1) + ": " + str(result) + '\n')	

def main():
	inp()

main()
