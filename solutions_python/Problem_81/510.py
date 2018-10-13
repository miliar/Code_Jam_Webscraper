#!/usr/bin/python

def inp():
	fin=file('in.txt','r')
	fout=file('out.txt','a')
	testCases=fin.readline()
	for count in range(int(testCases)):
		cases=fin.readline()
		case=[]
		for i in range(int(cases)):
			case.append(fin.readline())
		result=compute(cases,case)
		out(count,result,fout,cases)

def compute(cases,case):
	win=[0]*int(cases)
	lose=[0]*int(cases)	
	for line in range(int(cases)):
		for num in range(int(cases)):
			if str(case[line][num])=="0":
				lose[line]=lose[line]+1
			elif str(case[line][num])=="1":
				win[line]=win[line]+1
	result=[]
	owp=[]
	wp=[]
	for roll in range(int(cases)):
		wp.append((float(win[roll])/(win[roll]+lose[roll])))
		owptmp=[]
		for ctr in range(int(cases)):
			if roll!=ctr:
				if str(case[ctr][roll])=="1":
					owptmp.append(float(win[ctr]-1)/(win[ctr]+lose[ctr]-1))
				elif str(case[ctr][roll])=="0":
					owptmp.append(float(win[ctr])/(win[ctr]+lose[ctr]-1))
				else:
					owptmp.append(float(0))
			else:
				owptmp.append(float(0))
		owpspare=0
		for add in range(int(cases)):
			owpspare=owpspare+owptmp[add]
		owp.append(float(owpspare)/(win[roll]+lose[roll]))
		result.append((0.25*wp[roll]+0.50*owp[roll]))
	oowp=[]
	for final in range(int(cases)):
		oowptmp=0
		for last in range(int(cases)):
			if str(case[final][last])!=".":
				oowptmp=oowptmp+owp[last]
		oowp.append(oowptmp/(win[final]+lose[final]))
		result[final]=result[final]+(0.25*oowp[final])
	return result

def out(count,result,fout,cases):
	fout.write("Case #" + str(count+1) + ": " + '\n')
	for line in range(int(cases)):
		fout.write(str(result[line]) + '\n')	

def main():
	inp()

main()
