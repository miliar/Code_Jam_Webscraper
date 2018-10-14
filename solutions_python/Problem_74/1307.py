import os

filename=os.sys.argv[1]
fp=open(filename,"r");
posC=[]
robo=[]
N=0
no_of_testcase=int(fp.readline())
for t in range(no_of_testcase):
	parmcount=0
	testcase=fp.readline()
	parm=testcase.split()
	#print parm
	N=int(parm[0])
	posC=[]
	robo=[]
	for i in range (1,2*N,2):
		robo.append(parm[i]);
		posC.append(int(parm[i+1]))	
	#print robo
	#print posC	
	lasttime=0
	lastposB=1
	lastposO=1	
	lasttimeO=0	
	lasttimeB=0
	timetoreachO=0
	timetoreachB=0
	for i in range(N):
		if(robo[i]== "B"):
			#print "lasttime in B" , lasttime
			temp=abs(lastposB-posC[i])+1;
			#print "tempB " , temp
			lastposB= posC[i];
			timetoreachB=lasttimeB+temp
			if(lasttime >= timetoreachB):
				lasttime=lasttime+1
			else:
				lasttime=lasttime+abs(lasttime-timetoreachB);
			
			lasttimeB=lasttime;
																																	
		elif(robo[i]== "O"):
			#print "lasttime in O" , lasttime
			temp=abs(lastposO-posC[i])+1;
			#print "tempO " , temp
			lastposO= posC[i];
			timetoreachO=lasttimeO+temp
			if(lasttime >= timetoreachO):
				lasttime=lasttime+1
			else:
				lasttime=lasttime+abs(lasttime-timetoreachO);
			
			lasttimeO=lasttime;
	print "Case #%s:" %str(t+1), lasttime
	

fp.close()	
