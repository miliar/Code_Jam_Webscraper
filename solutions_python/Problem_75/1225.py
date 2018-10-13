import os

filename=os.sys.argv[1]
fp=open(filename,"r");
patternC=[]
patternO=[]
outputlist =[]
C=0
N=0
no_of_testcase=int(fp.readline())
for t in range(no_of_testcase):
	parmcount=0
	testcase=fp.readline()
	parm=testcase.split()
	#print parm
	C=int(parm[0])
	j=0
	parmcount=1
	patternC=[]
	patternO=[]
	for i in range (parmcount, parmcount+C):
		temp= str(parm[i])
		patternC.append( temp[:-1])
		patternC.append(temp[-1])
		j=j+1
	parmcount=parmcount+C
	D=int(parm[parmcount])
	parmcount=parmcount+1	
	for i in range (parmcount,parmcount+D):
		patternO.append(parm[i])
	parmcount=parmcount+D	
	N= int(parm[parmcount]);
	
	inputstr=str(parm[parmcount+1]);
	#print C ,patternC,patternO, N, inputstr
	outputlist =[]
	for i in range(len(inputstr)):
		clearflag=0
		combine=0
		if (len(outputlist)):
			temp=outputlist[-1]+inputstr[i]	
			inx=-1
			inx1=-1
			try :
				inx=patternC.index(temp)
				outputlist.pop()
				outputlist.append(patternC[inx+1])
				combine=1
			except:
				try:
					inx1=patternC.index(temp[::-1])
					outputlist.pop()
					outputlist.append(patternC[inx1+1])	
					combine=1	
				except:
					combine=0
			templist=outputlist
			#print templist
			if not combine:
				for a in templist:
					#print a
					inx2=-1
					inx3=-1
					temp=a+inputstr[i]
					#print temp
					try:
						#print temp
						inx2=patternO.index(temp)
						#print "I m here4", inx2
						outputlist=[]
						clearflag=1
						break
					except:
						try:
							#print temp
	
							inx3=patternO.index(temp[::-1])
							#print "I m here3", inx3
							outputlist=[]
							clearflag=1
							break
						except:
							clearflag=0
				#print clearflag ,combine
			if ((not clearflag) and (not combine)):
				#print " I m here1"+ inputstr[i]
				outputlist.append(inputstr[i])
		else:
			#print " I m here"
			outputlist.append(inputstr[i])
	
	print "Case #%s: [" %str(t+1), ", ".join(map(str, outputlist)) +"]"
		
	
	
fp.close()	
