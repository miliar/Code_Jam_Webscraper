#!/usr/local/bin/python
fin=file("A-small-attempt0.in.txt")
fout=file("output.txt",'w')

casenum=int(fin.readline())

for n in range(0,casenum):

	frownum=int(fin.readline())

	for i in range(0,4):
		if i+1==frownum:
			frow=fin.readline()
		else:
			fin.readline()

	srownum=int(fin.readline())	

	for i in range(0,4):
		if i+1==srownum:
			srow=fin.readline()
		else:
			fin.readline()

	frowsp=srowsp=[]
	frowsp=frow.split()
	srowsp=srow.split()

	count=0

	for e in frowsp:
		if e in srowsp:
			count+=1
			result=e
	if count==1:
		fout.write('Case #%d: %s\n' %(n+1,result))
	elif count==0:
		fout.write('Case #%d: Volunteer cheated!\n' %(n+1))
	else:
		fout.write('Case #%d: Bad magician!\n' %(n+1))




